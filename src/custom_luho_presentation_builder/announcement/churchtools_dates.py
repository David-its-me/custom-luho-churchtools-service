import math
from churchtools.ct_client.ct_api_client import CTApiClient
from churchtools.ct_client.ct_calendar_fetcher import CTCalendarFetcher
from churchtools.ct_client.ct_event_fetcher import CTEventFetcher
from churchtools.ct_data_model.date.calendar_date import CalendarDate
from custom_luho_presentation_builder.announcement.churchtools_dates_data_service import (
    AnnouncementDatesDataService,
)
from date_services.calendar_preferences_manager import CalendarPreferencesManager
from propresenter.file_io import pro_assets
from propresenter.pb_auto_generated.presentation_pb2 import Presentation
from propresenter.pb_auto_generated.cue_pb2 import Cue
from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics
from propresenter.presentation_builder.standard_colors import *
from propresenter.presentation_builder.cue_builder import (
    createCue,
    generate_cue_group_from_cues,
)
from propresenter.presentation_builder.slide_builder import (
    create_slide_with_background_color,
)
from propresenter.presentation_builder.element_builder import image, rectangle, text


##################################
### CONFIG
##################################
icon_size = 60
icon_horizontal_space = 15
##################################


def __add_date_date_element(
    date: CalendarDate, slide: Slide, origin=Graphics.Point
) -> Slide:
    slide.elements.append(
        text(
            str(date.start_date.day),
            color=white(),
            bounds=Graphics.Rect(
                origin=origin,
                size=Graphics.Size(width=170, height=83),
            ),
            font=Graphics.Text.Attributes.Font(name="Roboto", size=50, bold=True),
            vertical_alignment=Graphics.Text.VERTICAL_ALIGNMENT_BOTTOM,
        )
    )
    slide.elements.append(
        text(
            date.start_date.get_month_abbreviation().upper(),
            color=black(),
            bounds=Graphics.Rect(
                origin=Graphics.Point(
                    x=origin.x,
                    y=origin.y + 83,
                ),
                size=Graphics.Size(width=170, height=83),
            ),
            vertical_alignment=Graphics.Text.VERTICAL_ALIGNMENT_TOP,
            font=Graphics.Text.Attributes.Font(
                name="Roboto",
                size=40,
            ),
        )
    )
    slide.elements.append(
        rectangle(
            bounds=Graphics.Rect(
                origin=origin, size=Graphics.Size(width=170, height=166)
            ),
            color=luho_gray(),
        )
    )
    return slide


def __add_date_headline(
    date: CalendarDate, slide: Slide, origin=Graphics.Point
) -> Slide:
    slide.elements.append(
        text(
            date.title.upper(),
            color=luho_blue_dark_theme(),
            bounds=Graphics.Rect(
                origin=origin,
                size=Graphics.Size(width=1458, height=60),
            ),
            font=Graphics.Text.Attributes.Font(
                name="Roboto",
                size=50,
            ),
            horizontal_alignment=Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_LEFT,
            vertical_alignment=Graphics.Text.VERTICAL_ALIGNMENT_TOP,
        )
    )
    return slide


def __add_icon(filename: str, slide: Slide, origin=Graphics.Point) -> Slide:

    pro_assets.move_from("./assets/icons", filename)
    slide.elements.append(
        image(
            pro_assets.get_relative_path(filename),
            bounds=Graphics.Rect(
                origin=origin, size=Graphics.Size(height=icon_size, width=icon_size)
            ),
        )
    )
    return slide


def __add_date_details_icons(
    date: CalendarDate, slide: Slide, origin=Graphics.Point
) -> Slide:

    slide = __add_icon("icon_children_white.png", slide, origin)
    origin = Graphics.Point(x=origin.x + icon_size + icon_horizontal_space, y=origin.y)
    slide = __add_icon("icon_communion_white.png", slide, origin)
    origin = Graphics.Point(x=origin.x + icon_size + icon_horizontal_space, y=origin.y)
    slide = __add_icon("icon_livestream.png", slide, origin)
    origin = Graphics.Point(x=origin.x + icon_size + icon_horizontal_space, y=origin.y)
    slide = __add_icon("icon_location_white.png", slide, origin)

    return slide


def __date_time_and_speaker_pretty_string(date: CalendarDate) -> str:
    hour = str(date.start_time.hour)
    minute = str(date.start_time.minute)
    while len(hour) < 2:
        hour = "0" + hour

    while len(minute) < 2:
        minute = "0" + minute

    return "{}:{} Uhr - mit {}".format(hour, minute, date.speaker)


def __add_date_time_and_speaker(date: CalendarDate, slide: Slide, origin=Graphics.Point) -> Slide:
    slide = __add_icon("icon_clock_white.png", slide, origin)
    origin = Graphics.Point(x=origin.x + icon_size + icon_horizontal_space, y=origin.y)
    slide.elements.append(
        text(
            __date_time_and_speaker_pretty_string(date),
            color=white(),
            bounds=Graphics.Rect(
                origin=origin,
                size=Graphics.Size(width=924, height=50),
            ),
            font=Graphics.Text.Attributes.Font(
                name="Roboto",
                size=40,
            ),
            horizontal_alignment=Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_LEFT,
            vertical_alignment=Graphics.Text.VERTICAL_ALIGNMENT_MIDDLE,
        )
    )
    return slide


def __add_date_element(
    date: CalendarDate, slide: Slide, origin=Graphics.Point
) -> Slide:

    slide = __add_date_date_element(date, slide, origin)
    origin_headline = Graphics.Point(
        x=origin.x + 210,
        y=origin.y - 10,
    )
    slide = __add_date_headline(
        date,
        slide,
        origin=origin_headline,
    )
    origin_details = Graphics.Point(
        x=origin_headline.x,
        y=origin_headline.y + 70,
    )
    slide = __add_date_time_and_speaker(date, slide, origin_details)
    origin_icons = Graphics.Point(x=origin_details.x, y=origin_details.y + 60)
    slide = __add_date_details_icons(date, slide, origin_icons)

    origin_underline = Graphics.Point(x=origin_icons.x, y=origin_icons.y + 60)
    slide.elements.append(
        rectangle(
            bounds=Graphics.Rect(
                origin=origin_underline,
                size=Graphics.Size(width=300, height=4),
            ),
            color=luho_gold(),
        )
    )

    return slide


def __date_slide(
    first_date: CalendarDate,
    second_date: CalendarDate,
    third_date: CalendarDate,
) -> Slide:
    slide = create_slide_with_background_color(black())

    slide.elements.append(
        text(
            "TERMINE",
            color=luho_blue_dark_theme(),
            bounds=Graphics.Rect(
                origin=Graphics.Point(
                    x=209,
                    y=114,
                ),
                size=Graphics.Size(width=1501, height=112),
            ),
            font=Graphics.Text.Attributes.Font(
                name="Roboto",
                size=103,
                bold=True,
            ),
            horizontal_alignment=Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_LEFT,
        )
    )
    if first_date is not None:
        slide = __add_date_element(
            first_date,
            slide,
            Graphics.Point(
                x=252,
                y=338,
            ),
        )
    if second_date is not None:
        slide = __add_date_element(
            second_date,
            slide,
            Graphics.Point(
                x=252,
                y=540,
            ),
        )
    if third_date is not None:
        slide = __add_date_element(
            third_date,
            slide,
            Graphics.Point(
                x=252,
                y=744,
            ),
        )
    return slide


def __get_date_slides(calendar_dates: CalendarDate) -> list[Slide]:
    number_of_slides_needed = math.ceil(len(calendar_dates) / 3)
    slides = []
    for i in range(number_of_slides_needed):
        if 3 * i < len(calendar_dates):
            first_date = calendar_dates[3 * i]
        else:
            first_date = None
        if 3 * i + 1 < len(calendar_dates):
            second_date = calendar_dates[3 * i + 1]
        else:
            second_date = None
        if 3 * i + 2 < len(calendar_dates):
            third_date = calendar_dates[3 * i + 2]
        else:
            third_date = None
        slide = __date_slide(
            first_date=first_date, second_date=second_date, third_date=third_date
        )
        slides.append(slide)

    return slides


def __load_events():
    ct_calendar_fetcher = CTCalendarFetcher()
    ct_event_fetcher = CTEventFetcher()
    calendar_preferences_manager = CalendarPreferencesManager(
        ct_calendar_fetcher=ct_calendar_fetcher
    )
    dates_data_service = AnnouncementDatesDataService(
        ct_calendar_fetcher=ct_calendar_fetcher,
        ct_event_fetcher=ct_event_fetcher,
        calendar_preferences_manager=calendar_preferences_manager,
    )

    calendar_dates = dates_data_service.get_upcoming_dates()
    return calendar_dates


def add_slides(presentation: Presentation, slide_duration: int) -> Presentation:
    calendar_dates = __load_events()
    print("Erstelle Termin Folien ...")
    print()
    cues: list[Cue] = []
    for slide in __get_date_slides(calendar_dates):
        cue = createCue(slide, completion_time=slide_duration)
        cues.append(cue)
        presentation.cues.append(cue)

    presentation.cue_groups.append(
        generate_cue_group_from_cues(
            cues, color=luho_blue(), label="Churchtools Kalender & Veranstaltungen"
        )
    )
    return presentation
