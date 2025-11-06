import math
from churchtools.ct_client.ct_api_client import CTApiClient
from churchtools.ct_client.ct_calendar_controller import CTCalendarController
from churchtools.ct_client.ct_event_controller import CTEventController
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
from propresenter.presentation_builder.cue_actions.macro import (
    create_announcement_macro,
)
from propresenter.presentation_builder.slide_element.chip import chip
from propresenter.presentation_builder.slide_element.image import image
from propresenter.presentation_builder.slide_element.rounded_rectangle import (
    empty_rounded_rectangle,
    rounded_rectangle,
)
from propresenter.presentation_builder.standard_colors import *
from propresenter.presentation_builder.cue import (
    createCue,
    generate_cue_group_from_cues,
)
from propresenter.presentation_builder.slide import (
    create_slide_with_background_color,
)
from propresenter.presentation_builder.slide_element.rectangle import rectangle
from propresenter.presentation_builder.slide_element.text import text


##################################
### CONFIG
##################################
icon_size = 60
icon_horizontal_space = 15
##################################


def __add_date_square_element(
    date: CalendarDate, slide: Slide, origin=Graphics.Point
) -> Slide:

    date_rectangle_size = 180

    slide.elements.append(
        text(
            str(date.start_date.day),
            color=white(),
            bounds=Graphics.Rect(
                origin=origin,
                size=Graphics.Size(
                    width=date_rectangle_size, height=date_rectangle_size
                ),
            ),
            font=Graphics.Text.Attributes.Font(name="Roboto", size=110, bold=True),
            vertical_alignment=Graphics.Text.VERTICAL_ALIGNMENT_BOTTOM,
        )
    )
    slide.elements.append(
        text(
            date.start_date.get_month_abbreviation(),
            color=white(),
            bounds=Graphics.Rect(
                origin=Graphics.Point(
                    x=origin.x,
                    y=origin.y + 18,
                ),
                size=Graphics.Size(width=date_rectangle_size, height=80),
            ),
            vertical_alignment=Graphics.Text.VERTICAL_ALIGNMENT_TOP,
            font=Graphics.Text.Attributes.Font(
                name="Roboto",
                size=35,
            ),
        )
    )
    slide.elements.append(
        rounded_rectangle(
            bounds=Graphics.Rect(
                origin=origin,
                size=Graphics.Size(
                    width=date_rectangle_size, height=date_rectangle_size
                ),
            ),
            color=dark_gray(),
            roundness=0.3,
        )
    )
    return slide


def __date_time_pretty_string(date: CalendarDate) -> str:
    hour = str(date.start_time.hour)
    minute = str(date.start_time.minute)
    while len(hour) < 2:
        hour = "0" + hour

    while len(minute) < 2:
        minute = "0" + minute

    time_pretty = "{}:{} UHR".format(hour, minute)

    return time_pretty


def __add_date_headline(
    date: CalendarDate, slide: Slide, origin=Graphics.Point
) -> Slide:
    slide.elements.append(
        text(
            "{} – {}".format(date.title.upper(), __date_time_pretty_string(date=date)),
            color=white(),
            bounds=Graphics.Rect(
                origin=origin,
                size=Graphics.Size(width=1458, height=60),
            ),
            font=Graphics.Text.Attributes.Font(name="Roboto", size=50, bold=True),
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

    color_hex_code = date.category_color.lstrip("#")
    red = int(color_hex_code[0:2], 16) / 255.0
    green = int(color_hex_code[2:4], 16) / 255.0
    blue = int(color_hex_code[4:6], 16) / 255.0

    if len(date.category) > 0:
        chip_element: Slide.Element = chip(
            text=date.category,
            color=Color(
                alpha=0.5,  # Let it appear like with less opacity. Christian Scharfschwert designed it with opacity 0.3, but the projector needs to be strong enough against the sunlight
                red=red,
                green=green,
                blue=blue,
            ),
            origin=Graphics.Point(y=origin.y + 5, x=origin.x),
        )
        slide.elements.append(chip_element)
        origin = Graphics.Point(
            y=origin.y,
            x=origin.x + chip_element.element.bounds.size.width + icon_horizontal_space,
        )
    if date.has_children_church:
        slide = __add_icon("icon_children_white.png", slide, origin)
        origin = Graphics.Point(
            x=origin.x + icon_size + icon_horizontal_space, y=origin.y
        )
    if date.has_communion:
        slide = __add_icon("icon_communion_white.png", slide, origin)
        origin = Graphics.Point(
            x=origin.x + icon_size + icon_horizontal_space, y=origin.y
        )
    if date.has_livestream:
        slide = __add_icon("icon_livestream.png", slide, origin)
        origin = Graphics.Point(
            x=origin.x + icon_size + icon_horizontal_space, y=origin.y
        )
    if len(date.location) > 0:
        slide = __add_icon("icon_location_white.png", slide, origin)
        origin = Graphics.Point(
            x=origin.x + icon_size + int(icon_horizontal_space / 2), y=origin.y
        )
        slide.elements.append(
            text(
                date.location,
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
        origin = Graphics.Point(
            x=origin.x + icon_size + icon_horizontal_space, y=origin.y
        )

    return slide


def __date_description_pretty_string(date: CalendarDate) -> str:
    if len(date.speaker) > 0:
        return "mit {}".format(date.speaker)
    else:
        return ""


def __add_date_description(
    date: CalendarDate, slide: Slide, origin=Graphics.Point
) -> Slide:
    slide.elements.append(
        text(
            __date_description_pretty_string(date),
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
    date: CalendarDate,
    slide: Slide,
    origin=Graphics.Point,
    hide_date_square: bool = False,
) -> Slide:

    if not hide_date_square:
        slide = __add_date_square_element(date, slide, origin)

    origin_headline = Graphics.Point(
        x=origin.x + 250,
        y=origin.y + 9,
    )
    slide = __add_date_headline(
        date,
        slide,
        origin=origin_headline,
    )
    origin_details = Graphics.Point(
        x=origin_headline.x,
        y=origin_headline.y + 61,
    )
    slide = __add_date_description(date, slide, origin_details)

    # place the icons higher if there is no description
    if len(__date_description_pretty_string(date)) == 0:
        origin_icons = Graphics.Point(x=origin_details.x, y=origin_details.y + 5)
    else:
        origin_icons = Graphics.Point(x=origin_details.x, y=origin_details.y + 52)

    slide = __add_date_details_icons(date, slide, origin_icons)

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
            color=white(),
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
    x_origin = 168
    if first_date is not None:
        slide = __add_date_element(
            first_date,
            slide,
            Graphics.Point(
                x=x_origin,
                y=300,
            ),
        )
    if second_date is not None:
        slide = __add_date_element(
            second_date,
            slide,
            Graphics.Point(
                x=x_origin,
                y=520,
            ),
            first_date.start_date.equals(second_date.start_date),
        )
    if third_date is not None:
        slide = __add_date_element(
            third_date,
            slide,
            Graphics.Point(
                x=x_origin,
                y=740,
            ),
            second_date.start_date.equals(third_date.start_date),
        )

    background_filename = "background_image.png"
    pro_assets.move_from("./assets/background", background_filename)
    slide.elements.append(
        image(
            pro_assets.get_relative_path(background_filename),
            bounds=Graphics.Rect(
                origin=Graphics.Point(x=0, y=0),
                size=Graphics.Size(height=1080, width=1920),
            ),
        )
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


def __load_events(ct_api_client: CTApiClient):
    ct_calendar_controller = CTCalendarController(ct_api_client.get_benste_uem_api())
    ct_event_controller = CTEventController(ct_api_client.get_benste_uem_api())
    calendar_preferences_manager = CalendarPreferencesManager(
        ct_calendar_controller=ct_calendar_controller
    )
    dates_data_service = AnnouncementDatesDataService(
        ct_calendar_controller=ct_calendar_controller,
        ct_event_controller=ct_event_controller,
        calendar_preferences_manager=calendar_preferences_manager,
    )

    calendar_dates = dates_data_service.get_upcoming_dates()
    return calendar_dates


def create(
    presentation: Presentation, slide_duration: int, ct_api_client: CTApiClient
) -> Presentation:
    calendar_dates = __load_events(ct_api_client)
    print("Erstelle Termin Folien")
    print()
    cues: list[Cue] = []
    for slide in __get_date_slides(calendar_dates):
        cue = createCue(
            slide, actions=[create_announcement_macro()], completion_time=slide_duration
        )
        cues.append(cue)
        presentation.cues.append(cue)

    presentation.cue_groups.append(
        generate_cue_group_from_cues(
            cues, color=luho_blue(), label="Churchtools Kalender & Veranstaltungen"
        )
    )
    return presentation
