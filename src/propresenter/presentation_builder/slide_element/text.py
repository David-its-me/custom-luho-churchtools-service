
from propresenter.pb_auto_generated.basicTypes_pb2 import Color
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics
from propresenter.presentation_builder.slide_element.helper.rtf_textfield import rtf_textfield
from propresenter.presentation_builder.slide_element.rectangle import empty_rectangle
from propresenter.presentation_builder.standard_colors import *


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