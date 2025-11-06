from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics
from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.presentation_builder.standard_colors import *
from propresenter.presentation_builder.uuid_generator import generate_random_uuid

def rounded_rectangle(
    bounds: Graphics.Rect = Graphics.Rect(
        origin=Graphics.Point(
            x=870,
            y=470,
        ),
        size=Graphics.Size(
            width=180,
            height=180,
        ),
    ),
    roundness=0.5,
    color: Color = blue()
) -> Slide.Element:
    slide_element = empty_rounded_rectangle(bounds=bounds, roundness=roundness)   
    slide_element.element.fill.CopyFrom(Graphics.Fill(color=color, enable=True))
    return slide_element


def empty_rounded_rectangle(
    bounds: Graphics.Rect = Graphics.Rect(
        origin=Graphics.Point(
            x=870,
            y=470,
        ),
        size=Graphics.Size(
            width=180,
            height=180,
        ),
    ),
    roundness=0.5,
) -> Slide.Element: 
    return Slide.Element(
        element=Graphics.Element(
            opacity=1,
            uuid=generate_random_uuid(),
            hidden=False,
            bounds=bounds,
            path=Graphics.Path(
                closed=True,
                shape=Graphics.Path.Shape(
                    type=Graphics.Path.Shape.TYPE_ROUNDED_RECTANGLE,
                    rounded_rectangle=Graphics.Path.Shape.RoundedRectangle(
                        roundness=roundness
                    ),
                ),
            ),
        ),
    )

