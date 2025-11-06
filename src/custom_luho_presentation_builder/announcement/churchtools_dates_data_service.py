from datetime import datetime, timedelta
import time
import json
from churchtools.ct_client.ct_calendar_controller import CTCalendarController
from churchtools.ct_client.ct_event_controller import CTEventController
from churchtools.ct_data_model.date.calendar_date import CalendarDate
from churchtools.ct_data_model.date.my_date import MyDate, fromIsoDate
from date_services.calendar_preferences_manager import CalendarPreferencesManager
from functools import cmp_to_key
import copy


class AnnouncementDatesDataService:

    def __init__(
        self,
        ct_calendar_controller: CTCalendarController,
        ct_event_controller: CTEventController,
        calendar_preferences_manager: CalendarPreferencesManager,
    ) -> None:
        self.ct_calendar_controller = ct_calendar_controller
        self.ct_event_controller = ct_event_controller
        self.calendar_preferences_manager: CalendarPreferencesManager = (
            calendar_preferences_manager
        )
        self.prettified_dates: list[CalendarDate] = None

    def __sort_dates(self, dates: list[CalendarDate]) -> list[CalendarDate]:
        sorted_dates: list[CalendarDate] = sorted(
            dates, key=cmp_to_key(lambda date1, date2: date2.is_start_before(date1))
        )
        return sorted_dates

    def __merge_dates(self, dates: list[CalendarDate]) -> list[CalendarDate]:
        # assume that the dates are already sorted, so only the neighbouring entries are compared.
        # Comparison is based on (1) date, (2) time and (3) title of the event.
        result: list[CalendarDate] = []
        for i in range(len(dates) - 1):
            if (
                dates[i].start_date.equals(dates[i + 1].start_date)
                and dates[i].start_time.equals(dates[i + 1].start_time)
                and dates[i].title == dates[i + 1].title
            ):

                # merge details
                # if details different concatenate and hope that the prettifier cleans it up
                if not dates[i].description == dates[i + 1].description:
                    dates[i + 1].description = "{} {}".format(
                        dates[i].description, dates[i + 1].description
                    )
                # if details different concatenate and hope that the prettifier cleans it up
                if not dates[i].speaker == dates[i + 1].speaker:
                    dates[i + 1].speaker = "{} {}".format(
                        dates[i].speaker, dates[i + 1].speaker
                    )
                # if details different concatenate and hope that the prettifier cleans it up
                if not dates[i].location == dates[i + 1].location:
                    dates[i + 1].location = "{} {}".format(
                        dates[i].location, dates[i + 1].location
                    )
                # if details different concatenate and hope that the prettifier cleans it up
                if not dates[i].sermontext == dates[i + 1].sermontext:
                    dates[i + 1].sermontext = "{} {}".format(
                        dates[i].sermontext, dates[i + 1].sermontext
                    )
                # if one entry has the defalt color, use the other (more specific) one
                if dates[i + 1].category_color == "#0560ab":
                    dates[i + 1].category_color == dates[i].category_color
                # if both entries have different colors the entry i+1 wins.

                # Booleans are concatenated with OR becaus the default value is always False
                dates[i + 1].is_event = dates[i].is_event or dates[i + 1].is_event
                dates[i + 1].has_livestream = (
                    dates[i].has_livestream or dates[i + 1].has_livestream
                )
                dates[i + 1].has_children_church = (
                    dates[i].has_children_church or dates[i + 1].has_children_church
                )
                dates[i + 1].has_communion = (
                    dates[i].has_communion or dates[i + 1].has_communion
                )
            else:
                result.append(dates[i])

        result.append(dates[len(dates) - 1])
        return result

    @staticmethod
    def _match_sequence(text: str, sequence: list[str]) -> (bool, dict):  # type: ignore
        text_copy: str = copy.deepcopy(text)  # because the text is manipulated
        if text_copy is None:
            text_copy = ""
        resulting_variable_matching = {}
        last_variable_name: str = None
        for fragment in sequence:
            fragment = fragment.lower().lstrip().rstrip()
            if fragment in text_copy.lower():
                # copy the content that will be cutted be the maching in the variable that stands before.
                start_index: int = text_copy.lower().find(fragment)
                split_index: int = start_index + len(fragment)
                if last_variable_name is not None:
                    variable = copy.deepcopy(text_copy[:start_index])
                    variable.lstrip()
                    if variable[1:].find(" ") != -1:
                        variable = variable[: variable[1:].find(" ") + 1]
                    if variable.find("\n") != -1:
                        variable = variable[: variable.find("\n")]
                    resulting_variable_matching[last_variable_name] = variable
                    last_variable_name = None
                # Cut the text up to the fragment matching point.
                text_copy = copy.deepcopy(text_copy[split_index:])
            # If there is a varaible, generate a new variable assignment
            elif fragment[:1] == "<" and fragment[-1:] == ">":
                tag_value: str = fragment[1:-1]
                if tag_value[:1] == "#":
                    last_variable_name = tag_value[1:]
                    resulting_variable_matching.update({last_variable_name: ""})
            else:
                return False, resulting_variable_matching

        # copy the content that will be cutted be the maching in the variable that stands before.
        if last_variable_name is not None:
            variable = copy.deepcopy(text_copy)
            variable.lstrip()
            if variable[1:].find(" ") != -1:
                variable = variable[: variable[1:].find(" ") + 1]
            if variable.find("\n") != -1:
                variable = variable[: variable.find("\n")]
            resulting_variable_matching[last_variable_name] = variable
            last_variable_name = None

        return (True, resulting_variable_matching)

    def __filter_dates(self, dates: list[CalendarDate]) -> list[CalendarDate]:
        result: list[CalendarDate] = []
        for date in dates:
            included: bool = True  # per default include events
            calendar_data = self.calendar_preferences_manager.get_calendar_config_by_id(
                date.category_id
            )
            if "filterRules" in calendar_data:
                if "includeTitles" in calendar_data["filterRules"]:
                    for titleIncludeRule in calendar_data["filterRules"][
                        "includeTitles"
                    ]:
                        (match, variables) = self._match_sequence(
                            date.title, titleIncludeRule
                        )
                        if match:
                            included = True
                            break

                if "excludeTitles" in calendar_data["filterRules"]:
                    for titleExcludeRule in calendar_data["filterRules"][
                        "excludeTitles"
                    ]:
                        (match, variables) = self._match_sequence(
                            date.title, titleExcludeRule
                        )
                        if match:
                            included = False
                            break

            else:  # if no rules are specified, then keep the date in the list per default -> optimistic
                included = True

            if included:
                result.append(date)

        return result

    @staticmethod
    def _apply_variable_assignment(
        value: str | bool, variabe_assignment: dict
    ) -> str | bool:
        if isinstance(value, str):
            if value.lstrip().rstrip()[:1] == "<" and value[-1:] == ">":
                tag_value: str = value.lstrip().rstrip()[1:-1]
                if tag_value[:1] == "#":
                    variable_name: str = tag_value[1:]
                    if variable_name in variabe_assignment:
                        return variabe_assignment[variable_name]
                    if variabe_assignment in variable_name:
                        return variabe_assignment[variable_name]
        return value

    @staticmethod
    def _apply_rule_manipulation(
        value: str | bool, rule: dict, variable_assignment: dict = {}
    ) -> str | bool:
        result: any = None
        if "replacement" in rule:
            result = rule["replacement"]
        if "addition" in rule:
            result = value + rule["addition"]
        if "value" in rule:
            result = rule["value"]

        if isinstance(result, str):
            return AnnouncementDatesDataService._apply_variable_assignment(
                value=result, variabe_assignment=variable_assignment
            )
        if isinstance(result, list):
            result_str: str = ""
            for fragment in result:
                result_str = (
                    result_str
                    + AnnouncementDatesDataService._apply_variable_assignment(
                        value=fragment, variabe_assignment=variable_assignment
                    )
                )
            return result_str

        return result

    @staticmethod
    def _replace_rule_tags_in_sequences(
        match_sequence: list[str], result_sequence: str | list, tag_definitions: dict
    ) -> list[dict]:
        result: list[dict] = []
        i: int = 0
        tag_found: bool = False
        for fragment in match_sequence:
            if fragment[:1] == "<" and fragment[-1:] == ">":
                tag_value: str = fragment[1:-1]
                if tag_value[:1] == "#":
                    variable_name: str = tag_value[1:]
                else:
                    tag_found = True
                    for tag_definition in tag_definitions:
                        if tag_definition["tagName"] == tag_value:
                            for tag_match in tag_definition["tagMatches"]:
                                # Handle a tag match
                                replaced_result_sequence = None
                                if isinstance(result_sequence, list):
                                    replaced_result_sequence = []
                                    replaced_result_sequence.extend(result_sequence)
                                    for j in range(len(replaced_result_sequence)):
                                        if replaced_result_sequence[j] == fragment:
                                            replaced_result_sequence[j] = tag_match[
                                                "value"
                                            ]
                                elif isinstance(result_sequence, str):
                                    replaced_result_sequence = result_sequence
                                    if replaced_result_sequence == fragment:
                                        replaced_result_sequence = tag_match["value"]

                                for match in tag_match["match"]:
                                    replaced_match_sequence: list[str] = []
                                    replaced_match_sequence.extend(match_sequence)
                                    replaced_match_sequence[i] = match
                                    ##### recursion step #####
                                    result.extend(
                                        AnnouncementDatesDataService._replace_rule_tags_in_sequences(
                                            replaced_match_sequence,
                                            replaced_result_sequence,
                                            tag_definitions=tag_definitions,
                                        )
                                    )
            i = i + 1

        if not tag_found:
            ##### This step is important to have a value at the end of the recursion #####
            result.append(
                {"matchSequence": match_sequence, "resultSequence": result_sequence}
            )

        return result

    @staticmethod
    def _tag_rule_with_given_sequences_names(
        rule: dict,
        match_sequence_name: str,
        result_sequence_name: str,
        tag_definitions: dict,
    ) -> list[dict]:
        resulting_rules: list = []
        if match_sequence_name in rule and result_sequence_name in rule:
            for (
                replaced_sequence
            ) in AnnouncementDatesDataService._replace_rule_tags_in_sequences(
                match_sequence=rule[match_sequence_name],
                result_sequence=rule[result_sequence_name],
                tag_definitions=tag_definitions,
            ):
                new_rule: dict = copy.deepcopy(rule)
                new_rule[match_sequence_name] = replaced_sequence["matchSequence"]
                new_rule[result_sequence_name] = replaced_sequence["resultSequence"]
                resulting_rules.append(new_rule)
        return resulting_rules

    @staticmethod
    def _tag_rule_with_given_match_sequence_name(
        rule: dict, match_sequence_name: str, tag_definitions: dict
    ) -> list[dict]:
        resulting_rules: list = []
        if "replacement" in rule:
            resulting_rules.extend(
                AnnouncementDatesDataService._tag_rule_with_given_sequences_names(
                    rule=rule,
                    match_sequence_name=match_sequence_name,
                    result_sequence_name="replacement",
                    tag_definitions=tag_definitions,
                )
            )
        if "addition" in rule:
            resulting_rules.extend(
                AnnouncementDatesDataService._tag_rule_with_given_sequences_names(
                    rule=rule,
                    match_sequence_name=match_sequence_name,
                    result_sequence_name="addition",
                    tag_definitions=tag_definitions,
                )
            )
        if "value" in rule:
            resulting_rules.extend(
                AnnouncementDatesDataService._tag_rule_with_given_sequences_names(
                    rule=rule,
                    match_sequence_name=match_sequence_name,
                    result_sequence_name="value",
                    tag_definitions=tag_definitions,
                )
            )
        return resulting_rules

    @staticmethod
    def _tag_rule(rule: dict, tag_definitions: dict) -> list[dict]:
        resulting_rules: list = []
        if "titleSequence" in rule:
            resulting_rules.extend(
                AnnouncementDatesDataService._tag_rule_with_given_match_sequence_name(
                    rule=rule,
                    match_sequence_name="titleSequence",
                    tag_definitions=tag_definitions,
                )
            )
        if "descriptionSequence" in rule:
            resulting_rules.extend(
                AnnouncementDatesDataService._tag_rule_with_given_match_sequence_name(
                    rule=rule,
                    match_sequence_name="descriptionSequence",
                    tag_definitions=tag_definitions,
                )
            )
        if "categorySequence" in rule:
            resulting_rules.extend(
                AnnouncementDatesDataService._tag_rule_with_given_match_sequence_name(
                    rule=rule,
                    match_sequence_name="categorySequence",
                    tag_definitions=tag_definitions,
                )
            )
        return resulting_rules

    @staticmethod
    def _process_rule(value: str | bool, rule: dict, date: CalendarDate) -> str | bool:
        if "titleSequence" in rule:
            (match, variable_assignment) = AnnouncementDatesDataService._match_sequence(
                date.title, rule["titleSequence"]
            )
            if match:
                value = AnnouncementDatesDataService._apply_rule_manipulation(
                    value=value, rule=rule, variable_assignment=variable_assignment
                )
        if "descriptionSequence" in rule:
            (match, variable_assignment) = AnnouncementDatesDataService._match_sequence(
                date.description, rule["descriptionSequence"]
            )
            if match:
                value = AnnouncementDatesDataService._apply_rule_manipulation(
                    value=value, rule=rule, variable_assignment=variable_assignment
                )
        if "categorySequence" in rule:
            (match, variable_assignment) = AnnouncementDatesDataService._match_sequence(
                date.category, rule["categorySequence"]
            )
            if match:
                value = AnnouncementDatesDataService._apply_rule_manipulation(
                    value=value, rule=rule, variable_assignment=variable_assignment
                )

        return value

    @staticmethod
    def _prettify_date(
        date: CalendarDate, rules: dict, tag_definitions: dict
    ) -> CalendarDate:
        # Title rules
        title_after_processing: str = copy.deepcopy(date.title)
        if "titleRules" in rules:
            for rule in rules["titleRules"]:
                for tagged_rule in AnnouncementDatesDataService._tag_rule(
                    rule=rule, tag_definitions=tag_definitions
                ):
                    title_after_processing = AnnouncementDatesDataService._process_rule(
                        title_after_processing, rule=tagged_rule, date=date
                    )
        # Description Rules
        description_after_processing: str = copy.deepcopy(date.description)
        if "descriptionRules" in rules:
            for rule in rules["descriptionRules"]:
                for tagged_rule in AnnouncementDatesDataService._tag_rule(
                    rule=rule, tag_definitions=tag_definitions
                ):
                    description_after_processing = (
                        AnnouncementDatesDataService._process_rule(
                            description_after_processing, rule=tagged_rule, date=date
                        )
                    )
        # Sermontext Rules
        sermontext_after_processing: str = copy.deepcopy(date.sermontext)
        if "sermontextRules" in rules:
            for rule in rules["sermontextRules"]:
                for tagged_rule in AnnouncementDatesDataService._tag_rule(
                    rule=rule, tag_definitions=tag_definitions
                ):
                    sermontext_after_processing = (
                        AnnouncementDatesDataService._process_rule(
                            sermontext_after_processing, rule=tagged_rule, date=date
                        )
                    )
        # Location Rules
        location_after_processing: str = copy.deepcopy(date.location)
        if "locationRules" in rules:
            for rule in rules["locationRules"]:
                for tagged_rule in AnnouncementDatesDataService._tag_rule(
                    rule=rule, tag_definitions=tag_definitions
                ):
                    location_after_processing = (
                        AnnouncementDatesDataService._process_rule(
                            location_after_processing, rule=tagged_rule, date=date
                        )
                    )
        # Category Rules
        category_after_processing: str = copy.deepcopy(date.category)
        if "categoryRules" in rules:
            for rule in rules["categoryRules"]:
                for tagged_rule in AnnouncementDatesDataService._tag_rule(
                    rule=rule, tag_definitions=tag_definitions
                ):
                    category_after_processing = (
                        AnnouncementDatesDataService._process_rule(
                            category_after_processing, rule=tagged_rule, date=date
                        )
                    )
        # Category Color Rules
        category_color_after_processing: str = copy.deepcopy(date.category_color)
        if "categoryColorRules" in rules:
            for rule in rules["categoryColorRules"]:
                for tagged_rule in AnnouncementDatesDataService._tag_rule(
                    rule=rule, tag_definitions=tag_definitions
                ):
                    category_color_after_processing = (
                        AnnouncementDatesDataService._process_rule(
                            category_color_after_processing, rule=tagged_rule, date=date
                        )
                    )
        # Communion Rules
        communion_after_processing: bool = copy.deepcopy(date.has_communion)
        if "hasCommunionRules" in rules:
            for rule in rules["hasCommunionRules"]:
                for tagged_rule in AnnouncementDatesDataService._tag_rule(
                    rule=rule, tag_definitions=tag_definitions
                ):
                    communion_after_processing = (
                        AnnouncementDatesDataService._process_rule(
                            communion_after_processing, rule=tagged_rule, date=date
                        )
                    )

        # After all rules are processed we can now apply the changes to the date
        date.title = title_after_processing
        date.description = description_after_processing
        date.sermontext = sermontext_after_processing
        date.location = location_after_processing
        date.category = category_after_processing
        date.category_color = category_color_after_processing
        date.has_communion = communion_after_processing

        return date

    def __prettify_dates(self, dates: list[CalendarDate]) -> list[CalendarDate]:
        tag_definitions: dict = []
        with open(
            "custom-configuration/prettify_rules_tag_definitions.json"
        ) as tag_definition_file:
            tag_definitions = json.load(tag_definition_file)

        with open("custom-configuration/prettify_rules.json") as file:
            rules: dict = json.load(file)
            for date in dates:
                date = AnnouncementDatesDataService._prettify_date(
                    date, rules=rules, tag_definitions=tag_definitions
                )
                date.pretty_print()

        return dates

    def get_upcoming_dates(self) -> list[CalendarDate]:

        dates: list[CalendarDate] = []

        today = datetime.now() + timedelta(days=0)
        # Calendar dates 1 week in advance
        max_date = today + timedelta(days=8)

        # Events - Load the next 12 events
        duration_event_polling = time.time()
        print("Lade Events von Churchtools ...")
        dates: list[CalendarDate] = self.ct_event_controller.get_events(12)
        duration_event_polling = time.time() - duration_event_polling

        # filter events by max_date
        dates = list(
            filter(
                lambda date: date.starts_before_datetime(max_date),
                dates,
            )
        )

        duration_date_polling = time.time()
        print("Lade Termine aus Kalendern von Churchtools ...")
        date_string_tomorrow: str = today.strftime("%Y-%m-%d")
        date_string_end: str = max_date.strftime("%Y-%m-%d")
        dates.extend(
            self.ct_calendar_controller.get_calendar_dates(
                from_=date_string_tomorrow,
                to_=date_string_end,
                calendar_ids=self.calendar_preferences_manager.get_visible_calendar_ids(),
            )
        )
        duration_date_polling = time.time() - duration_date_polling

        print("Bereite die Daten vor")
        print()

        # Sorting dates
        duration_sorting = time.time()
        sorted_dates: list[CalendarDate] = self.__sort_dates(dates)
        duration_sorting = time.time() - duration_sorting

        # Merge calendar with events if it is the same object
        duration_merging = time.time()
        merged_dates: list[CalendarDate] = self.__merge_dates(sorted_dates)
        duration_merging = time.time() - duration_merging

        # Filtering
        duration_filtering = time.time()
        filtered_dates: list[CalendarDate] = self.__filter_dates(merged_dates)
        duration_filtering = time.time() - duration_filtering

        # Prettify dates
        duration_prettify = time.time()
        self.prettified_dates = self.__prettify_dates(filtered_dates)
        duration_prettify = time.time() - duration_prettify

        with open("logs/time-measure.json", "w+") as time_measure_file:
            json.dump(
                {
                    "eventPolling": duration_event_polling,
                    "datePolling": duration_date_polling,
                    "sorting": duration_sorting,
                    "merging": duration_merging,
                    "filtering": duration_filtering,
                    "prettify": duration_prettify,
                },
                time_measure_file,
                indent=4,
            )

        return self.prettified_dates
