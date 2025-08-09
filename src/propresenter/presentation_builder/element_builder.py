from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics, Media
from propresenter.pb_auto_generated.basicTypes_pb2 import Color, URL
from propresenter.presentation_builder.uuid_builder import generate_random_uuid


def __text_scroller() -> Slide.Element.TextScroller:

    return Slide.Element.TextScroller(
        scroll_rate=0.5, should_repeat=True, repeat_distance=0.5
    )


def __element_text() -> Graphics.Text:
    # text_line_mask=Graphics.Text.LineFillMask(),
    return (
        Graphics.Text(
            attributes=Graphics.Text.Attributes(
                font=Graphics.Text.Attributes.Font(
                    name="ArialMT",
                    size=50,
                    family="Arial",
                    face="Regular",
                ),
                text_solid_fill=Color(alpha=1.0),
                paragraph_style=Graphics.Text.Attributes.Paragraph(
                    alignment=Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_CENTER,
                    line_height_multiple=1,
                    text_list=Graphics.Text.Attributes.Paragraph.TextList(),
                ),
                stroke_color=Color(red=1, green=0, blue=0, alpha=1),
            ),
            shadow=Graphics.Shadow(
                angle=315, offset=5, radius=5, color=Color(alpha=1), opacity=0.75
            ),
            vertical_alignment=Graphics.Text.VERTICAL_ALIGNMENT_MIDDLE,
            margins=Graphics.EdgeInsets(),
            is_superscript_standardized=True,
            transformDelimiter="  •  ",
            chord_pro=Graphics.Text.ChordPro(color=Color(alpha=1)),
        ),
    )


def image(image_path: str) -> Slide.Element:
    format = None
    if "." in image_path:
        format = image_path.split(".")[1]

    return Slide.Element(
        element=Graphics.Element(
            opacity=1,
            uuid=generate_random_uuid(),
            hidden=False,
            bounds=Graphics.Rect(
                origin=Graphics.Point(
                    x=0,
                    y=0,
                ),
                size=Graphics.Size(
                    width=1920,
                    height=1080,
                ),
            ),
            path=__default_bezier_path(),
            fill=Graphics.Fill(
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
                                )
                            )
                        )
                    )
                ),
            )
        ),
    )


def pink_box_element() -> Slide.Element:
    return Slide.Element(
        element=Graphics.Element(
            opacity=1,
            uuid=generate_random_uuid(),
            hidden=False,
            bounds=Graphics.Rect(
                origin=Graphics.Point(
                    x=870,
                    y=470,
                ),
                size=Graphics.Size(
                    width=180,
                    height=180,
                ),
            ),
            path=__default_bezier_path(),
            fill=Graphics.Fill(
                color=Color(
                    red=1,
                    green=0,
                    blue=1,
                    alpha=1,
                ),
                enable=True,
            ),
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
        ),
    )


def __default_bezier_path() -> Graphics.Path:
    return Graphics.Path(
            closed=True,
            shape=Graphics.Path.Shape(type=Graphics.Path.Shape.TYPE_RECTANGLE),
            points=[
                {
                    "point" : {
                        "x": 0.0,
                        "y": 0.0
                    },
                    "q0": {
                        "x": 0.0,
                        "y": 0.0
                    },
                    "q1": {
                        "x": 0.0,
                        "y": 0.0
                    }
                },
                {
                    "point" : {
                        "x": 1.0,
                        "y": 0.0
                    },
                    "q0": {
                        "x": 1.0,
                        "y": 0.0
                    },
                    "q1": {
                        "x": 1.0,
                        "y": 0.0
                    }
                },
                {
                    "point" : {
                        "x": 1.0,
                        "y": 1.0
                    },
                    "q0": {
                        "x": 1.0,
                        "y": 1.0
                    },
                    "q1": {
                        "x": 1.0,
                        "y": 1.0
                    }
                },
                {
                    "point" : {
                        "x": 0.0,
                        "y": 1.0
                    },
                    "q0": {
                        "x": 0.0,
                        "y": 1.0
                    },
                    "q1": {
                        "x": 0.0,
                        "y": 1.0
                    }
                }
            ]
        
    )
