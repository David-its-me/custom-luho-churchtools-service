
from propresenter.pb_auto_generated.basicTypes_pb2 import Color
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics
from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.presentation_builder.rtf_textfield import rtf_textfield
from propresenter.presentation_builder.rounded_rectangle_element_builder import empty_rounded_rectangle
from propresenter.presentation_builder.standard_colors import *



def __estimate_text_width(text: str, chip_height: float) -> float:
    return float((len(text) * 0.38 * chip_height) + chip_height + 30)


def chip(
    text: str,
    font: Graphics.Text.Attributes.Font = Graphics.Text.Attributes.Font(
        name="Roboto",
        size=40,
        family="Roboto",
        face="Regular",
        bold=False,
        italic=False,
    ),
    origin: Graphics.Point = Graphics.Point(
        x=240,
        y=135,
    ),
    text_color: Color = white(),
    stroke_color: Color = white(),
    color: Color = luho_gold(),
    margins: Graphics.EdgeInsets = Graphics.EdgeInsets(
        top=0, left=0, bottom=0, right=0
    ),
    horizontal_alignment: Graphics.Text.Attributes.Paragraph.Alignment = Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_CENTER,
    vertical_alignment: Graphics.Text = Graphics.Text.VERTICAL_ALIGNMENT_MIDDLE,
) -> Slide.Element:

    chip_hight: float = float(font.size + 10)
    bounds: Graphics.Rect = Graphics.Rect(
        origin=origin,
        size=Graphics.Size(
            width=__estimate_text_width(text, chip_hight),
            height=chip_hight,
        ),
    )
    slide_element = empty_rounded_rectangle(bounds=bounds, roundness=1)
    slide_element.element.fill.CopyFrom(Graphics.Fill(color=color, enable=True))
    slide_element.element.text.CopyFrom(
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
                color=text_color,
                margins=margins,
                stroke_color=stroke_color,
                background_color=transparent(),
                horizontal_alignment=horizontal_alignment,
            ),
        ),
    )

    return slide_element
