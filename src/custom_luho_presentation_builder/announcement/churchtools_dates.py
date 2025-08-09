
from propresenter.pb_auto_generated.presentation_pb2 import Presentation
from propresenter.pb_auto_generated.cue_pb2 import Cue
from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.pb_auto_generated.basicTypes_pb2 import Color
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics
from propresenter.presentation_builder.standard_colors import *
from propresenter.presentation_builder.cue_builder import (
    createCue,
    generate_cue_group_from_cues,
)
from propresenter.presentation_builder.slide_builder import (
    create_slide_with_background_color,
)
from propresenter.presentation_builder.element_builder import rectangle

##################################
### CONFIG
##################################
slide_duration = 10.0
##################################

def __date_slide() -> Slide:
    slide = create_slide_with_background_color(Color(
        red=1,
        green=1,
        blue=1,
        alpha=1
    ))
    slide.elements.append(rectangle(
        bounds=Graphics.Rect(
            origin=Graphics.Point(
                x=252,
                y=644,
            ),
            size=Graphics.Size(
                width=170,
                height=165
            )
        ),
        color=luho_gray()
    ))
    slide.elements.append(rectangle(
        bounds=Graphics.Rect(
            origin=Graphics.Point(
                x=252,
                y=440,
            ),
            size=Graphics.Size(
                width=170,
                height=165
            )
        ),
        color=luho_gray()
    ))
    slide.elements.append(rectangle(
        bounds=Graphics.Rect(
            origin=Graphics.Point(
                x=252,
                y=238,
            ),
            size=Graphics.Size(
                width=170,
                height=165
            )
        ),
        color=luho_gray()
    ))
    return slide

def __get_date_slides() -> list[Slide]:
    slide = __date_slide()
    return [slide]


def add_slides(presentation: Presentation) -> Presentation:
    print("Füge Kalender Folien hinzu")
    print()
    cues: list[Cue] = []
    for slide in __get_date_slides():
        cue = createCue(slide, completion_time=slide_duration)
        cues.append(cue)
        presentation.cues.append(cue)

    presentation.cue_groups.append(
        generate_cue_group_from_cues(
            cues, 
            color=luho_blue(),
            label="Churchtools Kalender & Veranstaltungen")
    )
    return presentation