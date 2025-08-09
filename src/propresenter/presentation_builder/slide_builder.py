from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.pb_auto_generated.basicTypes_pb2 import Color
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics
from propresenter.presentation_builder.uuid_builder import generate_random_uuid
import random


def createElement() -> Slide.Element:
    element = Slide.Element()
    return element


def create_random_background_color_slide() -> Slide:
    slide = create_empty_slide()
    slide.draws_background_color=True
    slide.background_color.CopyFrom(
        Color(
            blue=random.uniform(0, 1),
            red=random.uniform(0, 1),
            green=random.uniform(0, 1),
            alpha=1,
        )
    )
    return slide

def create_empty_slide() -> Slide:
    slide = Slide(
        size=Graphics.Size(height=1080, width=1920),
        uuid=generate_random_uuid(),
    )
    return slide
