from propresenter.pb_auto_generated.basicTypes_pb2 import Color
from propresenter.presentation_builder.standard_colors import *
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics


def rtf_textfield(
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
    horizontal_alignment: Graphics.Text.Attributes.Paragraph.Alignment=Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_CENTER,
) -> bytes:
    
    bold: str = "0"
    try:
        if font.bold:
            bold = ""
    except:
        pass
    
    italic: str = "0"
    try:
        if font.italic:
            italic = ""
    except:
        pass

    alignment: str = "c"
    if horizontal_alignment == Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_LEFT:
        alignment = "l"
    if horizontal_alignment == Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_CENTER:
        alignment = "c"
    if horizontal_alignment == Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_RIGHT:
        alignment = "r"
    if horizontal_alignment == Graphics.Text.Attributes.Paragraph.Alignment.ALIGNMENT_JUSTIFIED:
        alignment = "j"

    rtf_string = (
        "{\\rtf0\\ansi\\ansicpg1252"
        ### Font ###
        + "{\\fonttbl\\f0\\fnil "
        + font.name
        + ";}"
        ### Color table ###
        + "{\\colortbl;"
        ### Font Color ###
        + "\\red"
        + str(int(color.red * 255))
        + "\\green"
        + str(int(color.green * 255))
        + "\\blue"
        + str(int(color.blue * 255))
        + ";"
        ### Stroke Color
        + "\\red"
        + str(int(stroke_color.red * 255))
        + "\\green"
        + str(int(stroke_color.green * 255))
        + "\\blue"
        + str(int(stroke_color.blue * 255))
        + ";"
        ### background color ###
        + "\\red"
        + str(int(background_color.red * 255))
        + "\\green"
        + str(int(background_color.green * 255))
        + "\\blue"
        + str(int(background_color.blue * 255))
        + ";"
        + "}"

        + "{\\*"
        ### Expanded color table ###
        + "\\expandedcolortbl;"
        ### Font color ###
        + "\\csgenericrgb"
        + "\\c"
        + str(int(color.red * 100000))
        + "\\c"
        + str(int(color.green * 100000))
        + "\\c"
        + str(int(color.blue * 100000))
        + "\\c"
        + str(int(color.alpha * 100000))
        + ";"
        ### Stroke color ###
        + "\\csgenericrgb"
        + "\\c"
        + str(int(stroke_color.red * 100000))
        + "\\c"
        + str(int(stroke_color.green * 100000))
        + "\\c"
        + str(int(stroke_color.blue * 100000))
        + "\\c"
        + str(int(stroke_color.alpha * 100000))
        + ";"
        ### Background color ###
        + "\\csgenericrgb"
        + "\\c"
        + str(int(background_color.red * 100000))
        + "\\c"
        + str(int(background_color.green * 100000))
        + "\\c"
        + str(int(background_color.blue * 100000))
        + "\\c"
        + str(int(background_color.alpha * 100000))
        + ";"
        +"}"
        # + "{\\*\\listtable}"
        # + "{\\*\\listoverridetable}"
        ### Margins ###
        + "\\uc1\\paperw12240"
        + "\\margl"
        + str(int(margins.left * 20))
        + "\\margr"
        + str(int(margins.right * 20))
        + "\\margt"
        + str(int(margins.top * 20))
        + "\\margb"
        + str(int(margins.bottom * 20))
        + "\\pard\\li0\\fi0\\ri0"
        ### Horizontal alignment ###
        + "\\q" + alignment
        + "\\sb0\\sa0\\sl20\\slmult0\\slleading0"
        + "\\f0"
        ### Bold ###
        + "\\b" + bold
        ### Italic ###
        + "\\i" + italic
        + "\\ul0"
        + "\\strike0"
        + "\\fs"
        + str(int(font.size * 2))
        + "\\expnd0\\expndtw0\\CocoaLigature1\\cf1\\strokewidth0\\strokec2\\nosupersub\\ulc0\\highlight3\\cb3 "
        ### The text itself ###
        + text
        + "}"
    )

    return bytes(rtf_string, "utf-8")
