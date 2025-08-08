import basicTypes_pb2 as _basicTypes_pb2
import effects_pb2 as _effects_pb2
import digitalAudio_pb2 as _digitalAudio_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Graphics(_message.Message):
    __slots__ = ()
    class Element(_message.Message):
        __slots__ = ("uuid", "name", "bounds", "rotation", "opacity", "locked", "aspect_ratio_locked", "path", "fill", "stroke", "shadow", "feather", "text", "flipMode", "hidden", "text_line_mask")
        class FlipMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FLIP_MODE_NONE: _ClassVar[Graphics.Element.FlipMode]
            FLIP_MODE_VERTICAL: _ClassVar[Graphics.Element.FlipMode]
            FLIP_MODE_HORIZONTAL: _ClassVar[Graphics.Element.FlipMode]
            FLIP_MODE_BOTH: _ClassVar[Graphics.Element.FlipMode]
        FLIP_MODE_NONE: Graphics.Element.FlipMode
        FLIP_MODE_VERTICAL: Graphics.Element.FlipMode
        FLIP_MODE_HORIZONTAL: Graphics.Element.FlipMode
        FLIP_MODE_BOTH: Graphics.Element.FlipMode
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        BOUNDS_FIELD_NUMBER: _ClassVar[int]
        ROTATION_FIELD_NUMBER: _ClassVar[int]
        OPACITY_FIELD_NUMBER: _ClassVar[int]
        LOCKED_FIELD_NUMBER: _ClassVar[int]
        ASPECT_RATIO_LOCKED_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        FILL_FIELD_NUMBER: _ClassVar[int]
        STROKE_FIELD_NUMBER: _ClassVar[int]
        SHADOW_FIELD_NUMBER: _ClassVar[int]
        FEATHER_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        FLIPMODE_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_FIELD_NUMBER: _ClassVar[int]
        TEXT_LINE_MASK_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        bounds: Graphics.Rect
        rotation: float
        opacity: float
        locked: bool
        aspect_ratio_locked: bool
        path: Graphics.Path
        fill: Graphics.Fill
        stroke: Graphics.Stroke
        shadow: Graphics.Shadow
        feather: Graphics.Feather
        text: Graphics.Text
        flipMode: Graphics.Element.FlipMode
        hidden: bool
        text_line_mask: Graphics.Text.LineFillMask
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., bounds: _Optional[_Union[Graphics.Rect, _Mapping]] = ..., rotation: _Optional[float] = ..., opacity: _Optional[float] = ..., locked: bool = ..., aspect_ratio_locked: bool = ..., path: _Optional[_Union[Graphics.Path, _Mapping]] = ..., fill: _Optional[_Union[Graphics.Fill, _Mapping]] = ..., stroke: _Optional[_Union[Graphics.Stroke, _Mapping]] = ..., shadow: _Optional[_Union[Graphics.Shadow, _Mapping]] = ..., feather: _Optional[_Union[Graphics.Feather, _Mapping]] = ..., text: _Optional[_Union[Graphics.Text, _Mapping]] = ..., flipMode: _Optional[_Union[Graphics.Element.FlipMode, str]] = ..., hidden: bool = ..., text_line_mask: _Optional[_Union[Graphics.Text.LineFillMask, _Mapping]] = ...) -> None: ...
    class Rect(_message.Message):
        __slots__ = ("origin", "size")
        ORIGIN_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        origin: Graphics.Point
        size: Graphics.Size
        def __init__(self, origin: _Optional[_Union[Graphics.Point, _Mapping]] = ..., size: _Optional[_Union[Graphics.Size, _Mapping]] = ...) -> None: ...
    class Point(_message.Message):
        __slots__ = ("x", "y")
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        x: float
        y: float
        def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...
    class Size(_message.Message):
        __slots__ = ("width", "height")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: float
        height: float
        def __init__(self, width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...
    class EdgeInsets(_message.Message):
        __slots__ = ("left", "right", "top", "bottom")
        LEFT_FIELD_NUMBER: _ClassVar[int]
        RIGHT_FIELD_NUMBER: _ClassVar[int]
        TOP_FIELD_NUMBER: _ClassVar[int]
        BOTTOM_FIELD_NUMBER: _ClassVar[int]
        left: float
        right: float
        top: float
        bottom: float
        def __init__(self, left: _Optional[float] = ..., right: _Optional[float] = ..., top: _Optional[float] = ..., bottom: _Optional[float] = ...) -> None: ...
    class Path(_message.Message):
        __slots__ = ("closed", "points", "shape")
        class BezierPoint(_message.Message):
            __slots__ = ("point", "q0", "q1", "curved")
            POINT_FIELD_NUMBER: _ClassVar[int]
            Q0_FIELD_NUMBER: _ClassVar[int]
            Q1_FIELD_NUMBER: _ClassVar[int]
            CURVED_FIELD_NUMBER: _ClassVar[int]
            point: Graphics.Point
            q0: Graphics.Point
            q1: Graphics.Point
            curved: bool
            def __init__(self, point: _Optional[_Union[Graphics.Point, _Mapping]] = ..., q0: _Optional[_Union[Graphics.Point, _Mapping]] = ..., q1: _Optional[_Union[Graphics.Point, _Mapping]] = ..., curved: bool = ...) -> None: ...
        class Shape(_message.Message):
            __slots__ = ("type", "rounded_rectangle", "polygon", "star", "arrow")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TYPE_UNKNOWN: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_RECTANGLE: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_ELLIPSE: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_ISOSCELES_TRIANGLE: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_RIGHT_TRIANGLE: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_RHOMBUS: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_STAR: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_POLYGON: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_CUSTOM: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_RIGHT_ARROW: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_DOUBLE_ARROW: _ClassVar[Graphics.Path.Shape.Type]
                TYPE_ROUNDED_RECTANGLE: _ClassVar[Graphics.Path.Shape.Type]
            TYPE_UNKNOWN: Graphics.Path.Shape.Type
            TYPE_RECTANGLE: Graphics.Path.Shape.Type
            TYPE_ELLIPSE: Graphics.Path.Shape.Type
            TYPE_ISOSCELES_TRIANGLE: Graphics.Path.Shape.Type
            TYPE_RIGHT_TRIANGLE: Graphics.Path.Shape.Type
            TYPE_RHOMBUS: Graphics.Path.Shape.Type
            TYPE_STAR: Graphics.Path.Shape.Type
            TYPE_POLYGON: Graphics.Path.Shape.Type
            TYPE_CUSTOM: Graphics.Path.Shape.Type
            TYPE_RIGHT_ARROW: Graphics.Path.Shape.Type
            TYPE_DOUBLE_ARROW: Graphics.Path.Shape.Type
            TYPE_ROUNDED_RECTANGLE: Graphics.Path.Shape.Type
            class RoundedRectangle(_message.Message):
                __slots__ = ("roundness",)
                ROUNDNESS_FIELD_NUMBER: _ClassVar[int]
                roundness: float
                def __init__(self, roundness: _Optional[float] = ...) -> None: ...
            class Arrow(_message.Message):
                __slots__ = ("corner",)
                CORNER_FIELD_NUMBER: _ClassVar[int]
                corner: Graphics.Point
                def __init__(self, corner: _Optional[_Union[Graphics.Point, _Mapping]] = ...) -> None: ...
            class Polygon(_message.Message):
                __slots__ = ("number_sides",)
                NUMBER_SIDES_FIELD_NUMBER: _ClassVar[int]
                number_sides: int
                def __init__(self, number_sides: _Optional[int] = ...) -> None: ...
            class Star(_message.Message):
                __slots__ = ("inner_radius", "number_points")
                INNER_RADIUS_FIELD_NUMBER: _ClassVar[int]
                NUMBER_POINTS_FIELD_NUMBER: _ClassVar[int]
                inner_radius: float
                number_points: int
                def __init__(self, inner_radius: _Optional[float] = ..., number_points: _Optional[int] = ...) -> None: ...
            TYPE_FIELD_NUMBER: _ClassVar[int]
            ROUNDED_RECTANGLE_FIELD_NUMBER: _ClassVar[int]
            POLYGON_FIELD_NUMBER: _ClassVar[int]
            STAR_FIELD_NUMBER: _ClassVar[int]
            ARROW_FIELD_NUMBER: _ClassVar[int]
            type: Graphics.Path.Shape.Type
            rounded_rectangle: Graphics.Path.Shape.RoundedRectangle
            polygon: Graphics.Path.Shape.Polygon
            star: Graphics.Path.Shape.Star
            arrow: Graphics.Path.Shape.Arrow
            def __init__(self, type: _Optional[_Union[Graphics.Path.Shape.Type, str]] = ..., rounded_rectangle: _Optional[_Union[Graphics.Path.Shape.RoundedRectangle, _Mapping]] = ..., polygon: _Optional[_Union[Graphics.Path.Shape.Polygon, _Mapping]] = ..., star: _Optional[_Union[Graphics.Path.Shape.Star, _Mapping]] = ..., arrow: _Optional[_Union[Graphics.Path.Shape.Arrow, _Mapping]] = ...) -> None: ...
        CLOSED_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        SHAPE_FIELD_NUMBER: _ClassVar[int]
        closed: bool
        points: _containers.RepeatedCompositeFieldContainer[Graphics.Path.BezierPoint]
        shape: Graphics.Path.Shape
        def __init__(self, closed: bool = ..., points: _Optional[_Iterable[_Union[Graphics.Path.BezierPoint, _Mapping]]] = ..., shape: _Optional[_Union[Graphics.Path.Shape, _Mapping]] = ...) -> None: ...
    class Fill(_message.Message):
        __slots__ = ("enable", "color", "gradient", "media", "backgroundEffect")
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        GRADIENT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        BACKGROUNDEFFECT_FIELD_NUMBER: _ClassVar[int]
        enable: bool
        color: _basicTypes_pb2.Color
        gradient: Graphics.Gradient
        media: Media
        backgroundEffect: Graphics.BackgroundEffect
        def __init__(self, enable: bool = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., gradient: _Optional[_Union[Graphics.Gradient, _Mapping]] = ..., media: _Optional[_Union[Media, _Mapping]] = ..., backgroundEffect: _Optional[_Union[Graphics.BackgroundEffect, _Mapping]] = ...) -> None: ...
    class BackgroundEffect(_message.Message):
        __slots__ = ("backgroundBlur", "backgroundInvert")
        class BackgroundEffectBlur(_message.Message):
            __slots__ = ("saturation", "blur_amount")
            SATURATION_FIELD_NUMBER: _ClassVar[int]
            BLUR_AMOUNT_FIELD_NUMBER: _ClassVar[int]
            saturation: float
            blur_amount: float
            def __init__(self, saturation: _Optional[float] = ..., blur_amount: _Optional[float] = ...) -> None: ...
        class BackgroundEffectInvert(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        BACKGROUNDBLUR_FIELD_NUMBER: _ClassVar[int]
        BACKGROUNDINVERT_FIELD_NUMBER: _ClassVar[int]
        backgroundBlur: Graphics.BackgroundEffect.BackgroundEffectBlur
        backgroundInvert: Graphics.BackgroundEffect.BackgroundEffectInvert
        def __init__(self, backgroundBlur: _Optional[_Union[Graphics.BackgroundEffect.BackgroundEffectBlur, _Mapping]] = ..., backgroundInvert: _Optional[_Union[Graphics.BackgroundEffect.BackgroundEffectInvert, _Mapping]] = ...) -> None: ...
    class Gradient(_message.Message):
        __slots__ = ("type", "angle", "length", "stops")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_LINEAR: _ClassVar[Graphics.Gradient.Type]
            TYPE_RADIAL: _ClassVar[Graphics.Gradient.Type]
            TYPE_ANGLE: _ClassVar[Graphics.Gradient.Type]
        TYPE_LINEAR: Graphics.Gradient.Type
        TYPE_RADIAL: Graphics.Gradient.Type
        TYPE_ANGLE: Graphics.Gradient.Type
        class ColorStop(_message.Message):
            __slots__ = ("color", "position", "blend_point")
            COLOR_FIELD_NUMBER: _ClassVar[int]
            POSITION_FIELD_NUMBER: _ClassVar[int]
            BLEND_POINT_FIELD_NUMBER: _ClassVar[int]
            color: _basicTypes_pb2.Color
            position: float
            blend_point: float
            def __init__(self, color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., position: _Optional[float] = ..., blend_point: _Optional[float] = ...) -> None: ...
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ANGLE_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        STOPS_FIELD_NUMBER: _ClassVar[int]
        type: Graphics.Gradient.Type
        angle: float
        length: float
        stops: _containers.RepeatedCompositeFieldContainer[Graphics.Gradient.ColorStop]
        def __init__(self, type: _Optional[_Union[Graphics.Gradient.Type, str]] = ..., angle: _Optional[float] = ..., length: _Optional[float] = ..., stops: _Optional[_Iterable[_Union[Graphics.Gradient.ColorStop, _Mapping]]] = ...) -> None: ...
    class Shadow(_message.Message):
        __slots__ = ("style", "angle", "offset", "radius", "color", "opacity", "enable")
        class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STYLE_DROP: _ClassVar[Graphics.Shadow.Style]
        STYLE_DROP: Graphics.Shadow.Style
        STYLE_FIELD_NUMBER: _ClassVar[int]
        ANGLE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        RADIUS_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        OPACITY_FIELD_NUMBER: _ClassVar[int]
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        style: Graphics.Shadow.Style
        angle: float
        offset: float
        radius: float
        color: _basicTypes_pb2.Color
        opacity: float
        enable: bool
        def __init__(self, style: _Optional[_Union[Graphics.Shadow.Style, str]] = ..., angle: _Optional[float] = ..., offset: _Optional[float] = ..., radius: _Optional[float] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., opacity: _Optional[float] = ..., enable: bool = ...) -> None: ...
    class Stroke(_message.Message):
        __slots__ = ("style", "width", "color", "pattern", "enable")
        class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STYLE_SOLID_LINE: _ClassVar[Graphics.Stroke.Style]
            STYLE_SQUARE_DASH: _ClassVar[Graphics.Stroke.Style]
            STYLE_SHORT_DASH: _ClassVar[Graphics.Stroke.Style]
            STYLE_LONG_DASH: _ClassVar[Graphics.Stroke.Style]
        STYLE_SOLID_LINE: Graphics.Stroke.Style
        STYLE_SQUARE_DASH: Graphics.Stroke.Style
        STYLE_SHORT_DASH: Graphics.Stroke.Style
        STYLE_LONG_DASH: Graphics.Stroke.Style
        STYLE_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        PATTERN_FIELD_NUMBER: _ClassVar[int]
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        style: Graphics.Stroke.Style
        width: float
        color: _basicTypes_pb2.Color
        pattern: _containers.RepeatedScalarFieldContainer[float]
        enable: bool
        def __init__(self, style: _Optional[_Union[Graphics.Stroke.Style, str]] = ..., width: _Optional[float] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., pattern: _Optional[_Iterable[float]] = ..., enable: bool = ...) -> None: ...
    class Feather(_message.Message):
        __slots__ = ("style", "radius", "enable")
        class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STYLE_INSIDE: _ClassVar[Graphics.Feather.Style]
            STYLE_CENTER: _ClassVar[Graphics.Feather.Style]
            STYLE_OUTSIDE: _ClassVar[Graphics.Feather.Style]
        STYLE_INSIDE: Graphics.Feather.Style
        STYLE_CENTER: Graphics.Feather.Style
        STYLE_OUTSIDE: Graphics.Feather.Style
        STYLE_FIELD_NUMBER: _ClassVar[int]
        RADIUS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        style: Graphics.Feather.Style
        radius: float
        enable: bool
        def __init__(self, style: _Optional[_Union[Graphics.Feather.Style, str]] = ..., radius: _Optional[float] = ..., enable: bool = ...) -> None: ...
    class Text(_message.Message):
        __slots__ = ("attributes", "shadow", "rtf_data", "vertical_alignment", "scale_behavior", "margins", "is_superscript_standardized", "transform", "transformDelimiter", "chord_pro")
        class VerticalAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VERTICAL_ALIGNMENT_TOP: _ClassVar[Graphics.Text.VerticalAlignment]
            VERTICAL_ALIGNMENT_MIDDLE: _ClassVar[Graphics.Text.VerticalAlignment]
            VERTICAL_ALIGNMENT_BOTTOM: _ClassVar[Graphics.Text.VerticalAlignment]
        VERTICAL_ALIGNMENT_TOP: Graphics.Text.VerticalAlignment
        VERTICAL_ALIGNMENT_MIDDLE: Graphics.Text.VerticalAlignment
        VERTICAL_ALIGNMENT_BOTTOM: Graphics.Text.VerticalAlignment
        class ScaleBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_BEHAVIOR_NONE: _ClassVar[Graphics.Text.ScaleBehavior]
            SCALE_BEHAVIOR_ADJUST_CONTAINER_HEIGHT: _ClassVar[Graphics.Text.ScaleBehavior]
            SCALE_BEHAVIOR_SCALE_FONT_DOWN: _ClassVar[Graphics.Text.ScaleBehavior]
            SCALE_BEHAVIOR_SCALE_FONT_UP: _ClassVar[Graphics.Text.ScaleBehavior]
            SCALE_BEHAVIOR_SCALE_FONT_UP_DOWN: _ClassVar[Graphics.Text.ScaleBehavior]
        SCALE_BEHAVIOR_NONE: Graphics.Text.ScaleBehavior
        SCALE_BEHAVIOR_ADJUST_CONTAINER_HEIGHT: Graphics.Text.ScaleBehavior
        SCALE_BEHAVIOR_SCALE_FONT_DOWN: Graphics.Text.ScaleBehavior
        SCALE_BEHAVIOR_SCALE_FONT_UP: Graphics.Text.ScaleBehavior
        SCALE_BEHAVIOR_SCALE_FONT_UP_DOWN: Graphics.Text.ScaleBehavior
        class Transform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TRANSFORM_NONE: _ClassVar[Graphics.Text.Transform]
            TRANSFORM_SINGLE_LINE: _ClassVar[Graphics.Text.Transform]
            TRANSFORM_ONE_WORD_PER_LINE: _ClassVar[Graphics.Text.Transform]
            TRANSFORM_ONE_CHARACTER_PER_LINE: _ClassVar[Graphics.Text.Transform]
            TRANSFORM_REPLACE_LINE_RETURNS: _ClassVar[Graphics.Text.Transform]
        TRANSFORM_NONE: Graphics.Text.Transform
        TRANSFORM_SINGLE_LINE: Graphics.Text.Transform
        TRANSFORM_ONE_WORD_PER_LINE: Graphics.Text.Transform
        TRANSFORM_ONE_CHARACTER_PER_LINE: Graphics.Text.Transform
        TRANSFORM_REPLACE_LINE_RETURNS: Graphics.Text.Transform
        class LineFillMask(_message.Message):
            __slots__ = ("enabled", "height_offset", "vertical_offset", "mask_style", "width_offset", "horizontal_offset")
            class LineMaskStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                LINE_MASK_STYLE_FULL_WIDTH: _ClassVar[Graphics.Text.LineFillMask.LineMaskStyle]
                LINE_MASK_STYLE_LINE_WIDTH: _ClassVar[Graphics.Text.LineFillMask.LineMaskStyle]
                LINE_MASK_STYLE_MAX_LINE_WIDTH: _ClassVar[Graphics.Text.LineFillMask.LineMaskStyle]
            LINE_MASK_STYLE_FULL_WIDTH: Graphics.Text.LineFillMask.LineMaskStyle
            LINE_MASK_STYLE_LINE_WIDTH: Graphics.Text.LineFillMask.LineMaskStyle
            LINE_MASK_STYLE_MAX_LINE_WIDTH: Graphics.Text.LineFillMask.LineMaskStyle
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            HEIGHT_OFFSET_FIELD_NUMBER: _ClassVar[int]
            VERTICAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
            MASK_STYLE_FIELD_NUMBER: _ClassVar[int]
            WIDTH_OFFSET_FIELD_NUMBER: _ClassVar[int]
            HORIZONTAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            height_offset: float
            vertical_offset: float
            mask_style: Graphics.Text.LineFillMask.LineMaskStyle
            width_offset: float
            horizontal_offset: float
            def __init__(self, enabled: bool = ..., height_offset: _Optional[float] = ..., vertical_offset: _Optional[float] = ..., mask_style: _Optional[_Union[Graphics.Text.LineFillMask.LineMaskStyle, str]] = ..., width_offset: _Optional[float] = ..., horizontal_offset: _Optional[float] = ...) -> None: ...
        class GradientFill(_message.Message):
            __slots__ = ("gradient", "stretch_to_document_bounds")
            GRADIENT_FIELD_NUMBER: _ClassVar[int]
            STRETCH_TO_DOCUMENT_BOUNDS_FIELD_NUMBER: _ClassVar[int]
            gradient: Graphics.Gradient
            stretch_to_document_bounds: bool
            def __init__(self, gradient: _Optional[_Union[Graphics.Gradient, _Mapping]] = ..., stretch_to_document_bounds: bool = ...) -> None: ...
        class CutOutFill(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class MediaFill(_message.Message):
            __slots__ = ("media", "use_object_bounds")
            MEDIA_FIELD_NUMBER: _ClassVar[int]
            USE_OBJECT_BOUNDS_FIELD_NUMBER: _ClassVar[int]
            media: Media
            use_object_bounds: bool
            def __init__(self, media: _Optional[_Union[Media, _Mapping]] = ..., use_object_bounds: bool = ...) -> None: ...
        class ChordPro(_message.Message):
            __slots__ = ("enabled", "notation", "color")
            class Notation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NOTATION_CHORDS: _ClassVar[Graphics.Text.ChordPro.Notation]
                NOTATION_NUMBERS: _ClassVar[Graphics.Text.ChordPro.Notation]
                NOTATION_NUMERALS: _ClassVar[Graphics.Text.ChordPro.Notation]
                NOTATION_DO_RE_MI: _ClassVar[Graphics.Text.ChordPro.Notation]
            NOTATION_CHORDS: Graphics.Text.ChordPro.Notation
            NOTATION_NUMBERS: Graphics.Text.ChordPro.Notation
            NOTATION_NUMERALS: Graphics.Text.ChordPro.Notation
            NOTATION_DO_RE_MI: Graphics.Text.ChordPro.Notation
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            NOTATION_FIELD_NUMBER: _ClassVar[int]
            COLOR_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            notation: Graphics.Text.ChordPro.Notation
            color: _basicTypes_pb2.Color
            def __init__(self, enabled: bool = ..., notation: _Optional[_Union[Graphics.Text.ChordPro.Notation, str]] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ...) -> None: ...
        class Attributes(_message.Message):
            __slots__ = ("font", "capitalization", "underline_style", "underline_color", "paragraph_style", "kerning", "superscript", "strikethrough_style", "strikethrough_color", "stroke_width", "stroke_color", "custom_attributes", "background_color", "text_solid_fill", "text_gradient_fill", "cut_out_fill", "media_fill", "background_effect")
            class Capitalization(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CAPITALIZATION_NONE: _ClassVar[Graphics.Text.Attributes.Capitalization]
                CAPITALIZATION_ALL_CAPS: _ClassVar[Graphics.Text.Attributes.Capitalization]
                CAPITALIZATION_SMALL_CAPS: _ClassVar[Graphics.Text.Attributes.Capitalization]
                CAPITALIZATION_TITLE_CASE: _ClassVar[Graphics.Text.Attributes.Capitalization]
                CAPITALIZATION_START_CASE: _ClassVar[Graphics.Text.Attributes.Capitalization]
            CAPITALIZATION_NONE: Graphics.Text.Attributes.Capitalization
            CAPITALIZATION_ALL_CAPS: Graphics.Text.Attributes.Capitalization
            CAPITALIZATION_SMALL_CAPS: Graphics.Text.Attributes.Capitalization
            CAPITALIZATION_TITLE_CASE: Graphics.Text.Attributes.Capitalization
            CAPITALIZATION_START_CASE: Graphics.Text.Attributes.Capitalization
            class Font(_message.Message):
                __slots__ = ("name", "size", "italic", "bold", "family", "face")
                NAME_FIELD_NUMBER: _ClassVar[int]
                SIZE_FIELD_NUMBER: _ClassVar[int]
                ITALIC_FIELD_NUMBER: _ClassVar[int]
                BOLD_FIELD_NUMBER: _ClassVar[int]
                FAMILY_FIELD_NUMBER: _ClassVar[int]
                FACE_FIELD_NUMBER: _ClassVar[int]
                name: str
                size: float
                italic: bool
                bold: bool
                family: str
                face: str
                def __init__(self, name: _Optional[str] = ..., size: _Optional[float] = ..., italic: bool = ..., bold: bool = ..., family: _Optional[str] = ..., face: _Optional[str] = ...) -> None: ...
            class Underline(_message.Message):
                __slots__ = ("style", "pattern", "by_word")
                class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    STYLE_NONE: _ClassVar[Graphics.Text.Attributes.Underline.Style]
                    STYLE_SINGLE: _ClassVar[Graphics.Text.Attributes.Underline.Style]
                    STYLE_THICK: _ClassVar[Graphics.Text.Attributes.Underline.Style]
                    STYLE_DOUBLE: _ClassVar[Graphics.Text.Attributes.Underline.Style]
                STYLE_NONE: Graphics.Text.Attributes.Underline.Style
                STYLE_SINGLE: Graphics.Text.Attributes.Underline.Style
                STYLE_THICK: Graphics.Text.Attributes.Underline.Style
                STYLE_DOUBLE: Graphics.Text.Attributes.Underline.Style
                class Pattern(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    PATTERN_SOLID: _ClassVar[Graphics.Text.Attributes.Underline.Pattern]
                    PATTERN_DOT: _ClassVar[Graphics.Text.Attributes.Underline.Pattern]
                    PATTERN_DASH: _ClassVar[Graphics.Text.Attributes.Underline.Pattern]
                    PATTERN_DASH_DOT: _ClassVar[Graphics.Text.Attributes.Underline.Pattern]
                    PATTERN_DASH_DOT_DOT: _ClassVar[Graphics.Text.Attributes.Underline.Pattern]
                PATTERN_SOLID: Graphics.Text.Attributes.Underline.Pattern
                PATTERN_DOT: Graphics.Text.Attributes.Underline.Pattern
                PATTERN_DASH: Graphics.Text.Attributes.Underline.Pattern
                PATTERN_DASH_DOT: Graphics.Text.Attributes.Underline.Pattern
                PATTERN_DASH_DOT_DOT: Graphics.Text.Attributes.Underline.Pattern
                STYLE_FIELD_NUMBER: _ClassVar[int]
                PATTERN_FIELD_NUMBER: _ClassVar[int]
                BY_WORD_FIELD_NUMBER: _ClassVar[int]
                style: Graphics.Text.Attributes.Underline.Style
                pattern: Graphics.Text.Attributes.Underline.Pattern
                by_word: bool
                def __init__(self, style: _Optional[_Union[Graphics.Text.Attributes.Underline.Style, str]] = ..., pattern: _Optional[_Union[Graphics.Text.Attributes.Underline.Pattern, str]] = ..., by_word: bool = ...) -> None: ...
            class Paragraph(_message.Message):
                __slots__ = ("alignment", "first_line_head_indent", "head_indent", "tail_indent", "line_height_multiple", "maximum_line_height", "minimum_line_height", "line_spacing", "paragraph_spacing", "paragraph_spacing_before", "tab_stops", "default_tab_interval", "text_list", "text_lists")
                class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    ALIGNMENT_LEFT: _ClassVar[Graphics.Text.Attributes.Paragraph.Alignment]
                    ALIGNMENT_RIGHT: _ClassVar[Graphics.Text.Attributes.Paragraph.Alignment]
                    ALIGNMENT_CENTER: _ClassVar[Graphics.Text.Attributes.Paragraph.Alignment]
                    ALIGNMENT_JUSTIFIED: _ClassVar[Graphics.Text.Attributes.Paragraph.Alignment]
                    ALIGNMENT_NATURAL: _ClassVar[Graphics.Text.Attributes.Paragraph.Alignment]
                ALIGNMENT_LEFT: Graphics.Text.Attributes.Paragraph.Alignment
                ALIGNMENT_RIGHT: Graphics.Text.Attributes.Paragraph.Alignment
                ALIGNMENT_CENTER: Graphics.Text.Attributes.Paragraph.Alignment
                ALIGNMENT_JUSTIFIED: Graphics.Text.Attributes.Paragraph.Alignment
                ALIGNMENT_NATURAL: Graphics.Text.Attributes.Paragraph.Alignment
                class TabStop(_message.Message):
                    __slots__ = ("location", "alignment")
                    class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                        __slots__ = ()
                        ALIGNMENT_LEFT: _ClassVar[Graphics.Text.Attributes.Paragraph.TabStop.Alignment]
                        ALIGNMENT_RIGHT: _ClassVar[Graphics.Text.Attributes.Paragraph.TabStop.Alignment]
                        ALIGNMENT_CENTER: _ClassVar[Graphics.Text.Attributes.Paragraph.TabStop.Alignment]
                        ALIGNMENT_JUSTIFIED: _ClassVar[Graphics.Text.Attributes.Paragraph.TabStop.Alignment]
                        ALIGNMENT_NATURAL: _ClassVar[Graphics.Text.Attributes.Paragraph.TabStop.Alignment]
                    ALIGNMENT_LEFT: Graphics.Text.Attributes.Paragraph.TabStop.Alignment
                    ALIGNMENT_RIGHT: Graphics.Text.Attributes.Paragraph.TabStop.Alignment
                    ALIGNMENT_CENTER: Graphics.Text.Attributes.Paragraph.TabStop.Alignment
                    ALIGNMENT_JUSTIFIED: Graphics.Text.Attributes.Paragraph.TabStop.Alignment
                    ALIGNMENT_NATURAL: Graphics.Text.Attributes.Paragraph.TabStop.Alignment
                    LOCATION_FIELD_NUMBER: _ClassVar[int]
                    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
                    location: float
                    alignment: Graphics.Text.Attributes.Paragraph.TabStop.Alignment
                    def __init__(self, location: _Optional[float] = ..., alignment: _Optional[_Union[Graphics.Text.Attributes.Paragraph.TabStop.Alignment, str]] = ...) -> None: ...
                class TextList(_message.Message):
                    __slots__ = ("is_enabled", "number_type", "prefix", "postfix", "starting_number")
                    class NumberType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                        __slots__ = ()
                        NUMBER_TYPE_BOX: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_CHECK: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_CIRCLE: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_DIAMOND: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_DISC: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_HYPHEN: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_SQUARE: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_DECIMAL: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_LOWERCASE_ALPHA: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_UPPERCASE_ALPHA: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_LOWERCASE_ROMAN: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                        NUMBER_TYPE_UPPERCASE_ROMAN: _ClassVar[Graphics.Text.Attributes.Paragraph.TextList.NumberType]
                    NUMBER_TYPE_BOX: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_CHECK: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_CIRCLE: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_DIAMOND: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_DISC: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_HYPHEN: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_SQUARE: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_DECIMAL: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_LOWERCASE_ALPHA: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_UPPERCASE_ALPHA: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_LOWERCASE_ROMAN: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    NUMBER_TYPE_UPPERCASE_ROMAN: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
                    NUMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
                    PREFIX_FIELD_NUMBER: _ClassVar[int]
                    POSTFIX_FIELD_NUMBER: _ClassVar[int]
                    STARTING_NUMBER_FIELD_NUMBER: _ClassVar[int]
                    is_enabled: bool
                    number_type: Graphics.Text.Attributes.Paragraph.TextList.NumberType
                    prefix: str
                    postfix: str
                    starting_number: int
                    def __init__(self, is_enabled: bool = ..., number_type: _Optional[_Union[Graphics.Text.Attributes.Paragraph.TextList.NumberType, str]] = ..., prefix: _Optional[str] = ..., postfix: _Optional[str] = ..., starting_number: _Optional[int] = ...) -> None: ...
                ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
                FIRST_LINE_HEAD_INDENT_FIELD_NUMBER: _ClassVar[int]
                HEAD_INDENT_FIELD_NUMBER: _ClassVar[int]
                TAIL_INDENT_FIELD_NUMBER: _ClassVar[int]
                LINE_HEIGHT_MULTIPLE_FIELD_NUMBER: _ClassVar[int]
                MAXIMUM_LINE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
                MINIMUM_LINE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
                LINE_SPACING_FIELD_NUMBER: _ClassVar[int]
                PARAGRAPH_SPACING_FIELD_NUMBER: _ClassVar[int]
                PARAGRAPH_SPACING_BEFORE_FIELD_NUMBER: _ClassVar[int]
                TAB_STOPS_FIELD_NUMBER: _ClassVar[int]
                DEFAULT_TAB_INTERVAL_FIELD_NUMBER: _ClassVar[int]
                TEXT_LIST_FIELD_NUMBER: _ClassVar[int]
                TEXT_LISTS_FIELD_NUMBER: _ClassVar[int]
                alignment: Graphics.Text.Attributes.Paragraph.Alignment
                first_line_head_indent: float
                head_indent: float
                tail_indent: float
                line_height_multiple: float
                maximum_line_height: float
                minimum_line_height: float
                line_spacing: float
                paragraph_spacing: float
                paragraph_spacing_before: float
                tab_stops: _containers.RepeatedCompositeFieldContainer[Graphics.Text.Attributes.Paragraph.TabStop]
                default_tab_interval: float
                text_list: Graphics.Text.Attributes.Paragraph.TextList
                text_lists: _containers.RepeatedCompositeFieldContainer[Graphics.Text.Attributes.Paragraph.TextList]
                def __init__(self, alignment: _Optional[_Union[Graphics.Text.Attributes.Paragraph.Alignment, str]] = ..., first_line_head_indent: _Optional[float] = ..., head_indent: _Optional[float] = ..., tail_indent: _Optional[float] = ..., line_height_multiple: _Optional[float] = ..., maximum_line_height: _Optional[float] = ..., minimum_line_height: _Optional[float] = ..., line_spacing: _Optional[float] = ..., paragraph_spacing: _Optional[float] = ..., paragraph_spacing_before: _Optional[float] = ..., tab_stops: _Optional[_Iterable[_Union[Graphics.Text.Attributes.Paragraph.TabStop, _Mapping]]] = ..., default_tab_interval: _Optional[float] = ..., text_list: _Optional[_Union[Graphics.Text.Attributes.Paragraph.TextList, _Mapping]] = ..., text_lists: _Optional[_Iterable[_Union[Graphics.Text.Attributes.Paragraph.TextList, _Mapping]]] = ...) -> None: ...
            class CustomAttribute(_message.Message):
                __slots__ = ("range", "capitalization", "original_font_size", "font_scale_factor", "text_gradient_fill", "should_preserve_foreground_color", "chord", "cut_out_fill", "media_fill", "background_effect")
                class Capitalization(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    CAPITALIZATION_NONE: _ClassVar[Graphics.Text.Attributes.CustomAttribute.Capitalization]
                    CAPITALIZATION_ALL_CAPS: _ClassVar[Graphics.Text.Attributes.CustomAttribute.Capitalization]
                    CAPITALIZATION_SMALL_CAPS: _ClassVar[Graphics.Text.Attributes.CustomAttribute.Capitalization]
                    CAPITALIZATION_TITLE_CASE: _ClassVar[Graphics.Text.Attributes.CustomAttribute.Capitalization]
                    CAPITALIZATION_START_CASE: _ClassVar[Graphics.Text.Attributes.CustomAttribute.Capitalization]
                CAPITALIZATION_NONE: Graphics.Text.Attributes.CustomAttribute.Capitalization
                CAPITALIZATION_ALL_CAPS: Graphics.Text.Attributes.CustomAttribute.Capitalization
                CAPITALIZATION_SMALL_CAPS: Graphics.Text.Attributes.CustomAttribute.Capitalization
                CAPITALIZATION_TITLE_CASE: Graphics.Text.Attributes.CustomAttribute.Capitalization
                CAPITALIZATION_START_CASE: Graphics.Text.Attributes.CustomAttribute.Capitalization
                RANGE_FIELD_NUMBER: _ClassVar[int]
                CAPITALIZATION_FIELD_NUMBER: _ClassVar[int]
                ORIGINAL_FONT_SIZE_FIELD_NUMBER: _ClassVar[int]
                FONT_SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
                TEXT_GRADIENT_FILL_FIELD_NUMBER: _ClassVar[int]
                SHOULD_PRESERVE_FOREGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
                CHORD_FIELD_NUMBER: _ClassVar[int]
                CUT_OUT_FILL_FIELD_NUMBER: _ClassVar[int]
                MEDIA_FILL_FIELD_NUMBER: _ClassVar[int]
                BACKGROUND_EFFECT_FIELD_NUMBER: _ClassVar[int]
                range: _basicTypes_pb2.IntRange
                capitalization: Graphics.Text.Attributes.CustomAttribute.Capitalization
                original_font_size: float
                font_scale_factor: float
                text_gradient_fill: Graphics.Text.GradientFill
                should_preserve_foreground_color: bool
                chord: str
                cut_out_fill: Graphics.Text.CutOutFill
                media_fill: Graphics.Text.MediaFill
                background_effect: Graphics.BackgroundEffect
                def __init__(self, range: _Optional[_Union[_basicTypes_pb2.IntRange, _Mapping]] = ..., capitalization: _Optional[_Union[Graphics.Text.Attributes.CustomAttribute.Capitalization, str]] = ..., original_font_size: _Optional[float] = ..., font_scale_factor: _Optional[float] = ..., text_gradient_fill: _Optional[_Union[Graphics.Text.GradientFill, _Mapping]] = ..., should_preserve_foreground_color: bool = ..., chord: _Optional[str] = ..., cut_out_fill: _Optional[_Union[Graphics.Text.CutOutFill, _Mapping]] = ..., media_fill: _Optional[_Union[Graphics.Text.MediaFill, _Mapping]] = ..., background_effect: _Optional[_Union[Graphics.BackgroundEffect, _Mapping]] = ...) -> None: ...
            FONT_FIELD_NUMBER: _ClassVar[int]
            CAPITALIZATION_FIELD_NUMBER: _ClassVar[int]
            UNDERLINE_STYLE_FIELD_NUMBER: _ClassVar[int]
            UNDERLINE_COLOR_FIELD_NUMBER: _ClassVar[int]
            PARAGRAPH_STYLE_FIELD_NUMBER: _ClassVar[int]
            KERNING_FIELD_NUMBER: _ClassVar[int]
            SUPERSCRIPT_FIELD_NUMBER: _ClassVar[int]
            STRIKETHROUGH_STYLE_FIELD_NUMBER: _ClassVar[int]
            STRIKETHROUGH_COLOR_FIELD_NUMBER: _ClassVar[int]
            STROKE_WIDTH_FIELD_NUMBER: _ClassVar[int]
            STROKE_COLOR_FIELD_NUMBER: _ClassVar[int]
            CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
            BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
            TEXT_SOLID_FILL_FIELD_NUMBER: _ClassVar[int]
            TEXT_GRADIENT_FILL_FIELD_NUMBER: _ClassVar[int]
            CUT_OUT_FILL_FIELD_NUMBER: _ClassVar[int]
            MEDIA_FILL_FIELD_NUMBER: _ClassVar[int]
            BACKGROUND_EFFECT_FIELD_NUMBER: _ClassVar[int]
            font: Graphics.Text.Attributes.Font
            capitalization: Graphics.Text.Attributes.Capitalization
            underline_style: Graphics.Text.Attributes.Underline
            underline_color: _basicTypes_pb2.Color
            paragraph_style: Graphics.Text.Attributes.Paragraph
            kerning: float
            superscript: int
            strikethrough_style: Graphics.Text.Attributes.Underline
            strikethrough_color: _basicTypes_pb2.Color
            stroke_width: float
            stroke_color: _basicTypes_pb2.Color
            custom_attributes: _containers.RepeatedCompositeFieldContainer[Graphics.Text.Attributes.CustomAttribute]
            background_color: _basicTypes_pb2.Color
            text_solid_fill: _basicTypes_pb2.Color
            text_gradient_fill: Graphics.Text.GradientFill
            cut_out_fill: Graphics.Text.CutOutFill
            media_fill: Graphics.Text.MediaFill
            background_effect: Graphics.BackgroundEffect
            def __init__(self, font: _Optional[_Union[Graphics.Text.Attributes.Font, _Mapping]] = ..., capitalization: _Optional[_Union[Graphics.Text.Attributes.Capitalization, str]] = ..., underline_style: _Optional[_Union[Graphics.Text.Attributes.Underline, _Mapping]] = ..., underline_color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., paragraph_style: _Optional[_Union[Graphics.Text.Attributes.Paragraph, _Mapping]] = ..., kerning: _Optional[float] = ..., superscript: _Optional[int] = ..., strikethrough_style: _Optional[_Union[Graphics.Text.Attributes.Underline, _Mapping]] = ..., strikethrough_color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., stroke_width: _Optional[float] = ..., stroke_color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., custom_attributes: _Optional[_Iterable[_Union[Graphics.Text.Attributes.CustomAttribute, _Mapping]]] = ..., background_color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., text_solid_fill: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., text_gradient_fill: _Optional[_Union[Graphics.Text.GradientFill, _Mapping]] = ..., cut_out_fill: _Optional[_Union[Graphics.Text.CutOutFill, _Mapping]] = ..., media_fill: _Optional[_Union[Graphics.Text.MediaFill, _Mapping]] = ..., background_effect: _Optional[_Union[Graphics.BackgroundEffect, _Mapping]] = ...) -> None: ...
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        SHADOW_FIELD_NUMBER: _ClassVar[int]
        RTF_DATA_FIELD_NUMBER: _ClassVar[int]
        VERTICAL_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        SCALE_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        MARGINS_FIELD_NUMBER: _ClassVar[int]
        IS_SUPERSCRIPT_STANDARDIZED_FIELD_NUMBER: _ClassVar[int]
        TRANSFORM_FIELD_NUMBER: _ClassVar[int]
        TRANSFORMDELIMITER_FIELD_NUMBER: _ClassVar[int]
        CHORD_PRO_FIELD_NUMBER: _ClassVar[int]
        attributes: Graphics.Text.Attributes
        shadow: Graphics.Shadow
        rtf_data: bytes
        vertical_alignment: Graphics.Text.VerticalAlignment
        scale_behavior: Graphics.Text.ScaleBehavior
        margins: Graphics.EdgeInsets
        is_superscript_standardized: bool
        transform: Graphics.Text.Transform
        transformDelimiter: str
        chord_pro: Graphics.Text.ChordPro
        def __init__(self, attributes: _Optional[_Union[Graphics.Text.Attributes, _Mapping]] = ..., shadow: _Optional[_Union[Graphics.Shadow, _Mapping]] = ..., rtf_data: _Optional[bytes] = ..., vertical_alignment: _Optional[_Union[Graphics.Text.VerticalAlignment, str]] = ..., scale_behavior: _Optional[_Union[Graphics.Text.ScaleBehavior, str]] = ..., margins: _Optional[_Union[Graphics.EdgeInsets, _Mapping]] = ..., is_superscript_standardized: bool = ..., transform: _Optional[_Union[Graphics.Text.Transform, str]] = ..., transformDelimiter: _Optional[str] = ..., chord_pro: _Optional[_Union[Graphics.Text.ChordPro, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class Media(_message.Message):
    __slots__ = ("uuid", "url", "metadata", "audio", "image", "video", "live_video", "web_content")
    class Metadata(_message.Message):
        __slots__ = ("manufacture_name", "manufacture_url", "information", "artist", "format")
        MANUFACTURE_NAME_FIELD_NUMBER: _ClassVar[int]
        MANUFACTURE_URL_FIELD_NUMBER: _ClassVar[int]
        INFORMATION_FIELD_NUMBER: _ClassVar[int]
        ARTIST_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        manufacture_name: str
        manufacture_url: _basicTypes_pb2.URL
        information: str
        artist: str
        format: str
        def __init__(self, manufacture_name: _Optional[str] = ..., manufacture_url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., information: _Optional[str] = ..., artist: _Optional[str] = ..., format: _Optional[str] = ...) -> None: ...
    class VideoDevice(_message.Message):
        __slots__ = ("type", "name", "unique_id", "model_id", "format_index", "audio_routing")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_GENERIC: _ClassVar[Media.VideoDevice.Type]
            TYPE_DIRECTSHOW: _ClassVar[Media.VideoDevice.Type]
            TYPE_BLACKMAGIC: _ClassVar[Media.VideoDevice.Type]
            TYPE_AJA: _ClassVar[Media.VideoDevice.Type]
            TYPE_AV: _ClassVar[Media.VideoDevice.Type]
            TYPE_SYPHON: _ClassVar[Media.VideoDevice.Type]
            TYPE_NDI: _ClassVar[Media.VideoDevice.Type]
            TYPE_BLUEFISH: _ClassVar[Media.VideoDevice.Type]
        TYPE_GENERIC: Media.VideoDevice.Type
        TYPE_DIRECTSHOW: Media.VideoDevice.Type
        TYPE_BLACKMAGIC: Media.VideoDevice.Type
        TYPE_AJA: Media.VideoDevice.Type
        TYPE_AV: Media.VideoDevice.Type
        TYPE_SYPHON: Media.VideoDevice.Type
        TYPE_NDI: Media.VideoDevice.Type
        TYPE_BLUEFISH: Media.VideoDevice.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
        MODEL_ID_FIELD_NUMBER: _ClassVar[int]
        FORMAT_INDEX_FIELD_NUMBER: _ClassVar[int]
        AUDIO_ROUTING_FIELD_NUMBER: _ClassVar[int]
        type: Media.VideoDevice.Type
        name: str
        unique_id: str
        model_id: str
        format_index: int
        audio_routing: _digitalAudio_pb2.DigitalAudio.Device.Routing
        def __init__(self, type: _Optional[_Union[Media.VideoDevice.Type, str]] = ..., name: _Optional[str] = ..., unique_id: _Optional[str] = ..., model_id: _Optional[str] = ..., format_index: _Optional[int] = ..., audio_routing: _Optional[_Union[_digitalAudio_pb2.DigitalAudio.Device.Routing, _Mapping]] = ...) -> None: ...
    class AudioDevice(_message.Message):
        __slots__ = ("name", "unique_id", "model_id", "channel_count")
        NAME_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
        MODEL_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
        name: str
        unique_id: str
        model_id: str
        channel_count: int
        def __init__(self, name: _Optional[str] = ..., unique_id: _Optional[str] = ..., model_id: _Optional[str] = ..., channel_count: _Optional[int] = ...) -> None: ...
    class Audio(_message.Message):
        __slots__ = ()
        class Channel(_message.Message):
            __slots__ = ("index", "muted", "volume", "compress_limit", "outputs")
            class Output(_message.Message):
                __slots__ = ("channel_index",)
                CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
                channel_index: int
                def __init__(self, channel_index: _Optional[int] = ...) -> None: ...
            INDEX_FIELD_NUMBER: _ClassVar[int]
            MUTED_FIELD_NUMBER: _ClassVar[int]
            VOLUME_FIELD_NUMBER: _ClassVar[int]
            COMPRESS_LIMIT_FIELD_NUMBER: _ClassVar[int]
            OUTPUTS_FIELD_NUMBER: _ClassVar[int]
            index: int
            muted: bool
            volume: float
            compress_limit: bool
            outputs: _containers.RepeatedCompositeFieldContainer[Media.Audio.Channel.Output]
            def __init__(self, index: _Optional[int] = ..., muted: bool = ..., volume: _Optional[float] = ..., compress_limit: bool = ..., outputs: _Optional[_Iterable[_Union[Media.Audio.Channel.Output, _Mapping]]] = ...) -> None: ...
        def __init__(self) -> None: ...
    class AudioProperties(_message.Message):
        __slots__ = ("volume", "audio_channels", "is_custom_mapping")
        VOLUME_FIELD_NUMBER: _ClassVar[int]
        AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        IS_CUSTOM_MAPPING_FIELD_NUMBER: _ClassVar[int]
        volume: float
        audio_channels: _containers.RepeatedCompositeFieldContainer[Media.Audio.Channel]
        is_custom_mapping: bool
        def __init__(self, volume: _Optional[float] = ..., audio_channels: _Optional[_Iterable[_Union[Media.Audio.Channel, _Mapping]]] = ..., is_custom_mapping: bool = ...) -> None: ...
    class TransportProperties(_message.Message):
        __slots__ = ("play_rate", "in_point", "out_point", "fade_in_duration", "fade_out_duration", "should_fade_in", "should_fade_out", "end_point", "playback_behavior", "loop_time", "times_to_loop")
        class PlaybackBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PLAYBACK_BEHAVIOR_STOP: _ClassVar[Media.TransportProperties.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_LOOP: _ClassVar[Media.TransportProperties.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT: _ClassVar[Media.TransportProperties.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: _ClassVar[Media.TransportProperties.PlaybackBehavior]
        PLAYBACK_BEHAVIOR_STOP: Media.TransportProperties.PlaybackBehavior
        PLAYBACK_BEHAVIOR_LOOP: Media.TransportProperties.PlaybackBehavior
        PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT: Media.TransportProperties.PlaybackBehavior
        PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: Media.TransportProperties.PlaybackBehavior
        PLAY_RATE_FIELD_NUMBER: _ClassVar[int]
        IN_POINT_FIELD_NUMBER: _ClassVar[int]
        OUT_POINT_FIELD_NUMBER: _ClassVar[int]
        FADE_IN_DURATION_FIELD_NUMBER: _ClassVar[int]
        FADE_OUT_DURATION_FIELD_NUMBER: _ClassVar[int]
        SHOULD_FADE_IN_FIELD_NUMBER: _ClassVar[int]
        SHOULD_FADE_OUT_FIELD_NUMBER: _ClassVar[int]
        END_POINT_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        LOOP_TIME_FIELD_NUMBER: _ClassVar[int]
        TIMES_TO_LOOP_FIELD_NUMBER: _ClassVar[int]
        play_rate: float
        in_point: float
        out_point: float
        fade_in_duration: float
        fade_out_duration: float
        should_fade_in: bool
        should_fade_out: bool
        end_point: float
        playback_behavior: Media.TransportProperties.PlaybackBehavior
        loop_time: float
        times_to_loop: int
        def __init__(self, play_rate: _Optional[float] = ..., in_point: _Optional[float] = ..., out_point: _Optional[float] = ..., fade_in_duration: _Optional[float] = ..., fade_out_duration: _Optional[float] = ..., should_fade_in: bool = ..., should_fade_out: bool = ..., end_point: _Optional[float] = ..., playback_behavior: _Optional[_Union[Media.TransportProperties.PlaybackBehavior, str]] = ..., loop_time: _Optional[float] = ..., times_to_loop: _Optional[int] = ...) -> None: ...
    class DrawingProperties(_message.Message):
        __slots__ = ("scale_behavior", "scale_alignment", "flipped_horizontally", "flipped_vertically", "natural_size", "custom_image_rotation", "custom_image_bounds", "custom_image_aspect_locked", "alpha_inverted", "native_rotation", "selected_effect_preset_uuid", "effects", "crop_enable", "crop_insets")
        class ScaleBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_BEHAVIOR_FIT: _ClassVar[Media.DrawingProperties.ScaleBehavior]
            SCALE_BEHAVIOR_FILL: _ClassVar[Media.DrawingProperties.ScaleBehavior]
            SCALE_BEHAVIOR_STRETCH: _ClassVar[Media.DrawingProperties.ScaleBehavior]
            SCALE_BEHAVIOR_CUSTOM: _ClassVar[Media.DrawingProperties.ScaleBehavior]
        SCALE_BEHAVIOR_FIT: Media.DrawingProperties.ScaleBehavior
        SCALE_BEHAVIOR_FILL: Media.DrawingProperties.ScaleBehavior
        SCALE_BEHAVIOR_STRETCH: Media.DrawingProperties.ScaleBehavior
        SCALE_BEHAVIOR_CUSTOM: Media.DrawingProperties.ScaleBehavior
        class ScaleAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_ALIGNMENT_MIDDLE_CENTER: _ClassVar[Media.DrawingProperties.ScaleAlignment]
            SCALE_ALIGNMENT_TOP_LEFT: _ClassVar[Media.DrawingProperties.ScaleAlignment]
            SCALE_ALIGNMENT_TOP_CENTER: _ClassVar[Media.DrawingProperties.ScaleAlignment]
            SCALE_ALIGNMENT_TOP_RIGHT: _ClassVar[Media.DrawingProperties.ScaleAlignment]
            SCALE_ALIGNMENT_MIDDLE_RIGHT: _ClassVar[Media.DrawingProperties.ScaleAlignment]
            SCALE_ALIGNMENT_BOTTOM_RIGHT: _ClassVar[Media.DrawingProperties.ScaleAlignment]
            SCALE_ALIGNMENT_BOTTOM_CENTER: _ClassVar[Media.DrawingProperties.ScaleAlignment]
            SCALE_ALIGNMENT_BOTTOM_LEFT: _ClassVar[Media.DrawingProperties.ScaleAlignment]
            SCALE_ALIGNMENT_MIDDLE_LEFT: _ClassVar[Media.DrawingProperties.ScaleAlignment]
        SCALE_ALIGNMENT_MIDDLE_CENTER: Media.DrawingProperties.ScaleAlignment
        SCALE_ALIGNMENT_TOP_LEFT: Media.DrawingProperties.ScaleAlignment
        SCALE_ALIGNMENT_TOP_CENTER: Media.DrawingProperties.ScaleAlignment
        SCALE_ALIGNMENT_TOP_RIGHT: Media.DrawingProperties.ScaleAlignment
        SCALE_ALIGNMENT_MIDDLE_RIGHT: Media.DrawingProperties.ScaleAlignment
        SCALE_ALIGNMENT_BOTTOM_RIGHT: Media.DrawingProperties.ScaleAlignment
        SCALE_ALIGNMENT_BOTTOM_CENTER: Media.DrawingProperties.ScaleAlignment
        SCALE_ALIGNMENT_BOTTOM_LEFT: Media.DrawingProperties.ScaleAlignment
        SCALE_ALIGNMENT_MIDDLE_LEFT: Media.DrawingProperties.ScaleAlignment
        class NativeRotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NATIVE_ROTATION_TYPE_ROTATE_STANDARD: _ClassVar[Media.DrawingProperties.NativeRotationType]
            NATIVE_ROTATION_TYPE_ROTATE_90: _ClassVar[Media.DrawingProperties.NativeRotationType]
            NATIVE_ROTATION_TYPE_ROTATE_180: _ClassVar[Media.DrawingProperties.NativeRotationType]
            NATIVE_ROTATION_TYPE_ROTATE_270: _ClassVar[Media.DrawingProperties.NativeRotationType]
        NATIVE_ROTATION_TYPE_ROTATE_STANDARD: Media.DrawingProperties.NativeRotationType
        NATIVE_ROTATION_TYPE_ROTATE_90: Media.DrawingProperties.NativeRotationType
        NATIVE_ROTATION_TYPE_ROTATE_180: Media.DrawingProperties.NativeRotationType
        NATIVE_ROTATION_TYPE_ROTATE_270: Media.DrawingProperties.NativeRotationType
        SCALE_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        SCALE_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        FLIPPED_HORIZONTALLY_FIELD_NUMBER: _ClassVar[int]
        FLIPPED_VERTICALLY_FIELD_NUMBER: _ClassVar[int]
        NATURAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_IMAGE_ROTATION_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_IMAGE_BOUNDS_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_IMAGE_ASPECT_LOCKED_FIELD_NUMBER: _ClassVar[int]
        ALPHA_INVERTED_FIELD_NUMBER: _ClassVar[int]
        NATIVE_ROTATION_FIELD_NUMBER: _ClassVar[int]
        SELECTED_EFFECT_PRESET_UUID_FIELD_NUMBER: _ClassVar[int]
        EFFECTS_FIELD_NUMBER: _ClassVar[int]
        CROP_ENABLE_FIELD_NUMBER: _ClassVar[int]
        CROP_INSETS_FIELD_NUMBER: _ClassVar[int]
        scale_behavior: Media.DrawingProperties.ScaleBehavior
        scale_alignment: Media.DrawingProperties.ScaleAlignment
        flipped_horizontally: bool
        flipped_vertically: bool
        natural_size: Graphics.Size
        custom_image_rotation: float
        custom_image_bounds: Graphics.Rect
        custom_image_aspect_locked: bool
        alpha_inverted: bool
        native_rotation: Media.DrawingProperties.NativeRotationType
        selected_effect_preset_uuid: _basicTypes_pb2.UUID
        effects: _containers.RepeatedCompositeFieldContainer[_effects_pb2.Effect]
        crop_enable: bool
        crop_insets: Graphics.EdgeInsets
        def __init__(self, scale_behavior: _Optional[_Union[Media.DrawingProperties.ScaleBehavior, str]] = ..., scale_alignment: _Optional[_Union[Media.DrawingProperties.ScaleAlignment, str]] = ..., flipped_horizontally: bool = ..., flipped_vertically: bool = ..., natural_size: _Optional[_Union[Graphics.Size, _Mapping]] = ..., custom_image_rotation: _Optional[float] = ..., custom_image_bounds: _Optional[_Union[Graphics.Rect, _Mapping]] = ..., custom_image_aspect_locked: bool = ..., alpha_inverted: bool = ..., native_rotation: _Optional[_Union[Media.DrawingProperties.NativeRotationType, str]] = ..., selected_effect_preset_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., effects: _Optional[_Iterable[_Union[_effects_pb2.Effect, _Mapping]]] = ..., crop_enable: bool = ..., crop_insets: _Optional[_Union[Graphics.EdgeInsets, _Mapping]] = ...) -> None: ...
    class VideoProperties(_message.Message):
        __slots__ = ("frame_rate", "field_type", "thumbnail_position", "end_behavior", "soft_loop", "soft_loop_duration")
        class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FIELD_TYPE_UNKNOWN: _ClassVar[Media.VideoProperties.FieldType]
            FIELD_TYPE_PROGRESSIVE: _ClassVar[Media.VideoProperties.FieldType]
            FIELD_TYPE_INTERLACED_UPPER_FIRST: _ClassVar[Media.VideoProperties.FieldType]
            FIELD_TYPE_INTERLACED_LOWER_FIRST: _ClassVar[Media.VideoProperties.FieldType]
        FIELD_TYPE_UNKNOWN: Media.VideoProperties.FieldType
        FIELD_TYPE_PROGRESSIVE: Media.VideoProperties.FieldType
        FIELD_TYPE_INTERLACED_UPPER_FIRST: Media.VideoProperties.FieldType
        FIELD_TYPE_INTERLACED_LOWER_FIRST: Media.VideoProperties.FieldType
        class EndBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            END_BEHAVIOR_STOP: _ClassVar[Media.VideoProperties.EndBehavior]
            END_BEHAVIOR_STOP_ON_BLACK: _ClassVar[Media.VideoProperties.EndBehavior]
            END_BEHAVIOR_STOP_ON_CLEAR: _ClassVar[Media.VideoProperties.EndBehavior]
            END_BEHAVIOR_FADE_TO_BLACK: _ClassVar[Media.VideoProperties.EndBehavior]
            END_BEHAVIOR_FADE_TO_CLEAR: _ClassVar[Media.VideoProperties.EndBehavior]
        END_BEHAVIOR_STOP: Media.VideoProperties.EndBehavior
        END_BEHAVIOR_STOP_ON_BLACK: Media.VideoProperties.EndBehavior
        END_BEHAVIOR_STOP_ON_CLEAR: Media.VideoProperties.EndBehavior
        END_BEHAVIOR_FADE_TO_BLACK: Media.VideoProperties.EndBehavior
        END_BEHAVIOR_FADE_TO_CLEAR: Media.VideoProperties.EndBehavior
        FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
        FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
        THUMBNAIL_POSITION_FIELD_NUMBER: _ClassVar[int]
        END_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        SOFT_LOOP_FIELD_NUMBER: _ClassVar[int]
        SOFT_LOOP_DURATION_FIELD_NUMBER: _ClassVar[int]
        frame_rate: float
        field_type: Media.VideoProperties.FieldType
        thumbnail_position: float
        end_behavior: Media.VideoProperties.EndBehavior
        soft_loop: bool
        soft_loop_duration: float
        def __init__(self, frame_rate: _Optional[float] = ..., field_type: _Optional[_Union[Media.VideoProperties.FieldType, str]] = ..., thumbnail_position: _Optional[float] = ..., end_behavior: _Optional[_Union[Media.VideoProperties.EndBehavior, str]] = ..., soft_loop: bool = ..., soft_loop_duration: _Optional[float] = ...) -> None: ...
    class LiveVideoProperties(_message.Message):
        __slots__ = ("video_device", "audio_device", "live_video_index")
        VIDEO_DEVICE_FIELD_NUMBER: _ClassVar[int]
        AUDIO_DEVICE_FIELD_NUMBER: _ClassVar[int]
        LIVE_VIDEO_INDEX_FIELD_NUMBER: _ClassVar[int]
        video_device: Media.VideoDevice
        audio_device: Media.AudioDevice
        live_video_index: int
        def __init__(self, video_device: _Optional[_Union[Media.VideoDevice, _Mapping]] = ..., audio_device: _Optional[_Union[Media.AudioDevice, _Mapping]] = ..., live_video_index: _Optional[int] = ...) -> None: ...
    class AudioTypeProperties(_message.Message):
        __slots__ = ("audio", "transport")
        AUDIO_FIELD_NUMBER: _ClassVar[int]
        TRANSPORT_FIELD_NUMBER: _ClassVar[int]
        audio: Media.AudioProperties
        transport: Media.TransportProperties
        def __init__(self, audio: _Optional[_Union[Media.AudioProperties, _Mapping]] = ..., transport: _Optional[_Union[Media.TransportProperties, _Mapping]] = ...) -> None: ...
    class ImageTypeProperties(_message.Message):
        __slots__ = ("drawing",)
        DRAWING_FIELD_NUMBER: _ClassVar[int]
        drawing: Media.DrawingProperties
        def __init__(self, drawing: _Optional[_Union[Media.DrawingProperties, _Mapping]] = ...) -> None: ...
    class VideoTypeProperties(_message.Message):
        __slots__ = ("drawing", "audio", "transport", "video")
        DRAWING_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FIELD_NUMBER: _ClassVar[int]
        TRANSPORT_FIELD_NUMBER: _ClassVar[int]
        VIDEO_FIELD_NUMBER: _ClassVar[int]
        drawing: Media.DrawingProperties
        audio: Media.AudioProperties
        transport: Media.TransportProperties
        video: Media.VideoProperties
        def __init__(self, drawing: _Optional[_Union[Media.DrawingProperties, _Mapping]] = ..., audio: _Optional[_Union[Media.AudioProperties, _Mapping]] = ..., transport: _Optional[_Union[Media.TransportProperties, _Mapping]] = ..., video: _Optional[_Union[Media.VideoProperties, _Mapping]] = ...) -> None: ...
    class LiveVideoTypeProperties(_message.Message):
        __slots__ = ("drawing", "audio", "live_video")
        DRAWING_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FIELD_NUMBER: _ClassVar[int]
        LIVE_VIDEO_FIELD_NUMBER: _ClassVar[int]
        drawing: Media.DrawingProperties
        audio: Media.AudioProperties
        live_video: Media.LiveVideoProperties
        def __init__(self, drawing: _Optional[_Union[Media.DrawingProperties, _Mapping]] = ..., audio: _Optional[_Union[Media.AudioProperties, _Mapping]] = ..., live_video: _Optional[_Union[Media.LiveVideoProperties, _Mapping]] = ...) -> None: ...
    class WebContentTypeProperties(_message.Message):
        __slots__ = ("drawing", "url")
        DRAWING_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        drawing: Media.DrawingProperties
        url: _basicTypes_pb2.URL
        def __init__(self, drawing: _Optional[_Union[Media.DrawingProperties, _Mapping]] = ..., url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    LIVE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    WEB_CONTENT_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    url: _basicTypes_pb2.URL
    metadata: Media.Metadata
    audio: Media.AudioTypeProperties
    image: Media.ImageTypeProperties
    video: Media.VideoTypeProperties
    live_video: Media.LiveVideoTypeProperties
    web_content: Media.WebContentTypeProperties
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., metadata: _Optional[_Union[Media.Metadata, _Mapping]] = ..., audio: _Optional[_Union[Media.AudioTypeProperties, _Mapping]] = ..., image: _Optional[_Union[Media.ImageTypeProperties, _Mapping]] = ..., video: _Optional[_Union[Media.VideoTypeProperties, _Mapping]] = ..., live_video: _Optional[_Union[Media.LiveVideoTypeProperties, _Mapping]] = ..., web_content: _Optional[_Union[Media.WebContentTypeProperties, _Mapping]] = ...) -> None: ...
