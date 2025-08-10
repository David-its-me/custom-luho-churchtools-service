import ast
import os
import logging
from datetime import datetime, timedelta, timezone
import pytz
import json
from churchtools_api.churchtools_api import ChurchToolsApi
from churchtools.ct_data_model.date.calendar_date import CalendarDate
from churchtools.ct_data_model.date.my_date import MyDate
from churchtools.ct_data_model.date.my_time import MyTime


class CTCalendarFetcher():
    
    def __init__(self):
        if 'CT_TOKEN' in os.environ:
            self.ct_token = os.environ['CT_TOKEN']
            self.ct_domain = os.environ['CT_DOMAIN']
            users_string = os.environ['CT_USERS']
            self.ct_users = ast.literal_eval(users_string)
            logging.info('using connection details provided with ENV variables')
        else:
            with open("secret/churchtools_credentials.json") as credential_file:
                secret_data = json.load(credential_file)
                self.ct_token = secret_data["ct_token"]
                self.ct_domain = secret_data["ct_domain"]
                self.ct_users = secret_data["ct_users"]
            logging.info('using connection details provided from secrets folder')

        self.api = ChurchToolsApi(domain=self.ct_domain, ct_token=self.ct_token)
    
    def _extract_date(self, isoDateString: str) -> MyDate:
        result_date = datetime.strptime(isoDateString, '%Y-%m-%dT%H:%M:%S%z').astimezone().date()
        return MyDate(
            day=result_date.day,
            month=result_date.month,
            year=result_date.year)
            #weekday=result_date.weekday)

    @staticmethod
    def _resolve_address_to_string(address: dict, note: str="") -> str:
        if note is None:
            note = ""
        note.lstrip().rstrip()
        if address is None:
            return note
        
        result: str = ""
        if "meetingAt" in address:
            if not address["meetingAt"] is None:
                if address["meetingAt"] == "":
                    result = result + note
                else:
                    result = result + address["meetingAt"]
        if "street" in address:
            if not address["street"] is None:
                result = result + ", " + address["street"]
        if "addition" in address:
            if not address["addition"] is None:
                result = result + " " + address["addition"]
        if "district" in address:
            if not address["district"] is None:
                result = result + " " + address["district"]
        if "zip" in address:
            if not address["zip"] is None:
                result = result + ", " + address["zip"]
        if "city" in address:
            if not address["city"] is None:
                result = result + " " + address["city"]
        if "country" in address:
            if not address["country"] is None:
                result = result + ", " + address["country"]
        return result
    
    def _extract_time(self, isoDateString: str) -> MyTime:
        result_time = datetime.strptime(isoDateString, '%Y-%m-%dT%H:%M:%S%z').astimezone(tz=timezone.utc)
        local_time = result_time.astimezone(pytz.timezone('Europe/Madrid'))
        return MyTime(
            hour=local_time.hour,
            minute=local_time.minute)
    
    

    
    def get_calendar_list(self) -> dict:
        """
        Tries to retrieve a list of calendars
        """
        result: dict = self.api.get_calendars()
        return result

    #TODO
    def get_calendar_dates(
            self, 
            from_: str, 
            to_: str, 
            calendar_ids: list) -> list[CalendarDate]:
        
        result: dict = self.api.get_calendar_appointments(
            calendar_ids=calendar_ids,
            from_=from_,
            to_=to_)
        
        dates: list[CalendarDate] = []

        for date in result:
            if not date["allDay"]: # Ignore dates without time (Ganztägig termine)
                description: str = date['information']
                if description is None:
                    description = ""
                newDate: CalendarDate = CalendarDate(
                    id=date["id"],
                    start_date=self._extract_date(date['startDate']),
                    start_time=self._extract_time(date['startDate']),
                    start_iso_datetime=date['startDate'],
                    end_iso_datetime=date['endDate'],
                    description=description,
                    end_date=self._extract_date(date['endDate']),
                    end_time=self._extract_time(date['endDate']),
                    title=date['caption'],
                    category=date['calendar']['name'],
                    is_event=False,
                    has_livestream=False,
                    has_childrenschurch=False,
                    has_communion=False,
                    location = self._resolve_address_to_string(address=date["address"], note=date["note"]),
                    sermontext = "",
                    speaker = "",
                    category_color = date['calendar']['color'],
                    category_id=date['calendar']['id']
                )
                dates.append(newDate)
            
        return dates
        

    def tearDown(self):
            """
            Destroy the session after test execution to avoid resource issues
            :return:
            """
            self.api.session.close()




