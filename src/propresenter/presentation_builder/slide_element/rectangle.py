from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics
from propresenter.pb_auto_generated.basicTypes_pb2 import Color
from propresenter.presentation_builder.uuid_generator import generate_random_uuid
from propresenter.presentation_builder.standard_colors import *



def empty_rectangle(
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
) -> Slide.Element:
    return Slide.Element(
        element=Graphics.Element(
            opacity=1,
            uuid=generate_random_uuid(),
            hidden=False,
            bounds=bounds,
            path=__default_bezier_path(),
        ),

    )


def rectangle(
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
    color: Color = pink(),
) -> Slide.Element:
    element = empty_rectangle(bounds=bounds)
    element.element.fill.CopyFrom(
        Graphics.Fill(
            color=color,
            enable=True,
        ),
    )
    return element


"""

            stroke=Graphics.Stroke(
                width=20,
                color=Color(
                    red=0,
                    green=1,
                    blue=0,
                    alpha=1,
                ),
                enable=True,
                style=Graphics.Stroke.Style.STYLE_SOLID_LINE,
            ),
"""


def __default_bezier_path() -> Graphics.Path:
    return Graphics.Path(
        closed=True,
        shape=Graphics.Path.Shape(type=Graphics.Path.Shape.TYPE_RECTANGLE),
        points=[
            {
                "point": {"x": 0.0, "y": 0.0},
                "q0": {"x": 0.0, "y": 0.0},
                "q1": {"x": 0.0, "y": 0.0},
            },
            {
                "point": {"x": 1.0, "y": 0.0},
                "q0": {"x": 1.0, "y": 0.0},
                "q1": {"x": 1.0, "y": 0.0},
            },
            {
                "point": {"x": 1.0, "y": 1.0},
                "q0": {"x": 1.0, "y": 1.0},
                "q1": {"x": 1.0, "y": 1.0},
            },
            {
                "point": {"x": 0.0, "y": 1.0},
                "q0": {"x": 0.0, "y": 1.0},
                "q1": {"x": 0.0, "y": 1.0},
            },
        ],
    )
