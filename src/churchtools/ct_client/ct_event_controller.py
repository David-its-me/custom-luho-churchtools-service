import ast
import os
import logging
from datetime import datetime, timezone
import pytz
import json
from churchtools_api.churchtools_api import ChurchToolsApi
from churchtools.ct_data_model.date.calendar_date import CalendarDate
from churchtools.ct_data_model.date.my_date import MyDate, fromIsoDate
from churchtools.ct_data_model.date.my_time import MyTime


class CTEventController():
    
    def __init__(self, api: ChurchToolsApi):
        self.api = api
        # On startup load all available services
        with open("custom-configuration/services.json", "w+") as services_file:
            json.dump(api.get_services(), services_file, indent=4)

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

    def get_services(self) -> dict:
        with open("custom-configuration/services.json") as services_file:
            try:
                return json.load(services_file)
            except: 
                pass
        return []
    
    def get_service_id_of(self, input_service_title: str) -> int:
        input_service_title = input_service_title.lower().rstrip().lstrip()
        for service in self.get_services():
            service_title = service['name']
            service_title = service_title.lower().rstrip().lstrip()
            if input_service_title in service_title:
                return service["id"]
            if service_title in input_service_title:
                return service["id"]
        return -1
    
    def has_livestream(self, event_id: int) -> bool:
        potential_service_names = ["stream", "live", "übertragung"]
        for service_name in potential_service_names:
            service_name_id: int = self.get_service_id_of(service_name)
            if service_name_id > -1:
                try:
                    service_count: int = self.api.get_event_services_counts_ajax(eventId=event_id, serviceId=service_name_id)[service_name_id]
                    if service_count > 0:
                        return True
                except:
                    pass
        return False
    
    def has_children_church(self, event_id: int) -> bool:
        potential_service_names = ["kinder", "kids", "kindergottesdienst"]
        for service_name in potential_service_names:
            service_name_id: int = self.get_service_id_of(service_name)
            if service_name_id > -1:
                try:
                    service_count: int = self.api.get_event_services_counts_ajax(eventId=event_id, serviceId=service_name_id)[service_name_id]
                    if service_count > 0:
                        return True
                except:
                    pass
        return False
    
    def has_communion(self, event_id: int) -> bool:
        potential_service_names = ["abendmahl", "abendmahlhelfer"]
        for service_name in potential_service_names:
            service_name_id: int = self.get_service_id_of(service_name)
            if service_name_id > -1:
                try:
                    service_count: int = self.api.get_event_services_counts_ajax(eventId=event_id, serviceId=service_name_id)[service_name_id]
                    if service_count > 0:
                        return True
                except:
                    pass
        return False

    def get_speaker(self, event_id: int):
        event_data: dict = self.api.get_AllEventData_ajax(event_id)

        potential_service_names = ["predigt", "referent", "speaker", "vortrag", "sprecher", "program", "liturgie", "moderation"]

        for service_name in potential_service_names:
            try:
                service_name_id: int = self.get_service_id_of(service_name)
                if service_name_id > -1:
                    if "services" in event_data:
                        if event_data["services"] is not None:
                            for service in event_data["services"]:
                                service_id: int = int(service["service_id"])
                                if service_id == service_name_id:
                                    if "name" in service:
                                        if service["name"] is not None:
                                            return service["name"]
            except:
                pass
        
        return ""
        

    def get_events(self, number_upcomming: int) -> list[CalendarDate]:
        # load next event (limit)
        result = self.api.get_events(limit=number_upcomming, direction='forward')

        events: list[CalendarDate] = []

        for event in result:
            #print(event)
            new_entry: CalendarDate = CalendarDate(
                id=event["appointmentId"],
                start_date=fromIsoDate(event['startDate']),
                start_time=self._extract_time(event['startDate']),
                start_iso_datetime=event['startDate'],
                end_iso_datetime=event['endDate'],
                description=event['description'],
                end_date=fromIsoDate(event['endDate']),
                end_time=self._extract_time(event['endDate']),
                title=event['name'],
                category=event['calendar']['title'],
                category_id=int(event['calendar']["domainIdentifier"]),
                is_event=True,
                speaker=self.get_speaker(event_id=event["id"]),
                sermon_text="",
                has_children_church=self.has_children_church(event_id=event["id"]),
                has_livestream=self.has_livestream(event_id=event["id"]),
                has_communion=self.has_communion(event_id=event["id"])
            )
            events.append(new_entry)
        
        return events
