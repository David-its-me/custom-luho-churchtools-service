from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.pb_auto_generated.basicTypes_pb2 import Color
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics
from propresenter.presentation_builder.uuid_generator import generate_random_uuid
from propresenter.presentation_builder.standard_colors import *


def createElement() -> Slide.Element:
    element = Slide.Element()
    return element


def create_slide_with_random_background_color() -> Slide:
    slide = create_slide_with_background_color(white())
    return slide


def create_slide_with_background_color(background_color: Color) -> Slide:
    slide = create_empty_slide()
    slide.draws_background_color = True
    slide.background_color.CopyFrom(background_color)
    return slide


def create_empty_slide() -> Slide:
    slide = Slide(
        size=Graphics.Size(height=1080, width=1920),
        uuid=generate_random_uuid(),
    )
    return slide
