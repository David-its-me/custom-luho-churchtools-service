from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics, Media
from propresenter.pb_auto_generated.basicTypes_pb2 import Color, URL
from propresenter.presentation_builder.uuid_builder import generate_random_uuid
from propresenter.presentation_builder.standard_colors import *
from propresenter.presentation_builder.rtf_textfield import *


def __text_scroller() -> Slide.Element.TextScroller:

    return Slide.Element.TextScroller(
        scroll_rate=0.5, should_repeat=True, repeat_distance=0.5
    )


def text(
    text: str,
    font=Graphics.Text.Attributes.Font(
        name="Roboto",
        size=50,
        family="Roboto",
        face="Regular",
        bold=False,
        italic=False,
    ),
    color: Color = black(),
    stroke_color: Color = white(),
    background_color: Color = transparent(),
    margins: Graphics.EdgeInsets = Graphics.EdgeInsets(
        top=0, left=0, bottom=0, right=0
    ),
    bounds: Graphics.Rect = Graphics.Rect(
        origin=Graphics.Point(
            x=240,
            y=135,
        ),
        size=Graphics.Size(
            width=1440,
            height=810,
        ),
    ),
    horizontal_alignment: Graphics.Text.Attributes.Paragraph.Alignment = Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_CENTER,
    vertical_alignment: Graphics.Text = Graphics.Text.VERTICAL_ALIGNMENT_MIDDLE,
) -> Graphics.Text:
    element = empty_rectangle(bounds=bounds)
    element.element.fill.CopyFrom(Graphics.Fill(color=white(), enable=False))
    # text_line_mask=Graphics.Text.LineFillMask(),
    element.element.text.CopyFrom(
        Graphics.Text(
            attributes=Graphics.Text.Attributes(
                font=font,
                stroke_color=stroke_color,
                # background_color=background_color,
                text_solid_fill=Color(alpha=1.0),
                paragraph_style=Graphics.Text.Attributes.Paragraph(
                    alignment=horizontal_alignment,
                    line_height_multiple=1,
                    # text_list=Graphics.Text.Attributes.Paragraph.TextList(),
                ),
            ),
            shadow=Graphics.Shadow(
                angle=315,
                offset=5,
                radius=5,
                color=Color(alpha=1),
                opacity=0.75,
                enable=False,
            ),
            vertical_alignment=vertical_alignment,
            margins=margins,
            is_superscript_standardized=True,
            transformDelimiter="  •  ",
            chord_pro=Graphics.Text.ChordPro(color=Color(alpha=1)),
            rtf_data=rtf_textfield(
                text=text,
                font=font,
                color=color,
                margins=margins,
                stroke_color=stroke_color,
                background_color=background_color,
                horizontal_alignment=horizontal_alignment,
            ),
        )
    )
    return element


def image(
    image_path: str,
    # Default bounds is a full HD slide
    bounds: Graphics.Rect = Graphics.Rect(
        origin=Graphics.Point(
            x=0,
            y=0,
        ),
        size=Graphics.Size(
            width=1920,
            height=1080,
        ),
    ),
) -> Slide.Element:
    format = None
    if "." in image_path:
        format = image_path.split(".")[1]

    element = empty_rectangle(bounds)
    element.element.fill.CopyFrom(
        Graphics.Fill(
            enable=True,
            media=Media(
                uuid=generate_random_uuid(),
                url=URL(
                    local=URL.LocalRelativePath(
                        root=URL.LocalRelativePath.Root.ROOT_SHOW,
                        path=image_path,
                    ),
                    platform=URL.Platform.PLATFORM_UNKNOWN,
                ),
                metadata=Media.Metadata(
                    format=format,
                ),
                image=Media.ImageTypeProperties(
                    drawing=Media.DrawingProperties(
                        custom_image_bounds=Graphics.Rect(
                            origin=Graphics.Point(
                                x=0.0,
                                y=0.0,
                            ),
                            size=Graphics.Size(
                                width=1920,
                                height=1080,
                            ),
                        )
                    )
                ),
            ),
        ),
    ),
    return element


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
