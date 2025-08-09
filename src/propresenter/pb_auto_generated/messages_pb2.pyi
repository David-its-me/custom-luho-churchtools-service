import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.templateIdentification_pb2 as _templateIdentification_pb2
import propresenter.pb_auto_generated.timers_pb2 as _timers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ("uuid", "title", "time_to_remove", "visible_on_network", "template", "clear_type", "message_text", "tokens", "token_values")
    class ClearType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLEAR_TYPE_MANUAL: _ClassVar[Message.ClearType]
        CLEAR_TYPE_AFTER_TIME: _ClassVar[Message.ClearType]
        CLEAR_TYPE_AFTER_TIMERS: _ClassVar[Message.ClearType]
    CLEAR_TYPE_MANUAL: Message.ClearType
    CLEAR_TYPE_AFTER_TIME: Message.ClearType
    CLEAR_TYPE_AFTER_TIMERS: Message.ClearType
    class Token(_message.Message):
        __slots__ = ("uuid", "text", "timer", "clock")
        class TokenTypeText(_message.Message):
            __slots__ = ("name",)
            NAME_FIELD_NUMBER: _ClassVar[int]
            name: str
            def __init__(self, name: _Optional[str] = ...) -> None: ...
        class TokenTypeTimer(_message.Message):
            __slots__ = ("name", "timer_uuid")
            NAME_FIELD_NUMBER: _ClassVar[int]
            TIMER_UUID_FIELD_NUMBER: _ClassVar[int]
            name: str
            timer_uuid: _basicTypes_pb2.UUID
            def __init__(self, name: _Optional[str] = ..., timer_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
        class TokenTypeClock(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        UUID_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        CLOCK_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        text: Message.Token.TokenTypeText
        timer: Message.Token.TokenTypeTimer
        clock: Message.Token.TokenTypeClock
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., text: _Optional[_Union[Message.Token.TokenTypeText, _Mapping]] = ..., timer: _Optional[_Union[Message.Token.TokenTypeTimer, _Mapping]] = ..., clock: _Optional[_Union[Message.Token.TokenTypeClock, _Mapping]] = ...) -> None: ...
    class TokenValue(_message.Message):
        __slots__ = ("token_id", "token_name", "text", "timer", "clock")
        class TokenValueText(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: str
            def __init__(self, value: _Optional[str] = ...) -> None: ...
        class TokenValueTimer(_message.Message):
            __slots__ = ("configuration", "format")
            CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
            FORMAT_FIELD_NUMBER: _ClassVar[int]
            configuration: _timers_pb2.Timer.Configuration
            format: _timers_pb2.Timer.Format
            def __init__(self, configuration: _Optional[_Union[_timers_pb2.Timer.Configuration, _Mapping]] = ..., format: _Optional[_Union[_timers_pb2.Timer.Format, _Mapping]] = ...) -> None: ...
        class TokenValueClock(_message.Message):
            __slots__ = ("format",)
            FORMAT_FIELD_NUMBER: _ClassVar[int]
            format: _timers_pb2.Clock.Format
            def __init__(self, format: _Optional[_Union[_timers_pb2.Clock.Format, _Mapping]] = ...) -> None: ...
        TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
        TOKEN_NAME_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        CLOCK_FIELD_NUMBER: _ClassVar[int]
        token_id: _basicTypes_pb2.UUID
        token_name: str
        text: Message.TokenValue.TokenValueText
        timer: Message.TokenValue.TokenValueTimer
        clock: Message.TokenValue.TokenValueClock
        def __init__(self, token_id: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., token_name: _Optional[str] = ..., text: _Optional[_Union[Message.TokenValue.TokenValueText, _Mapping]] = ..., timer: _Optional[_Union[Message.TokenValue.TokenValueTimer, _Mapping]] = ..., clock: _Optional[_Union[Message.TokenValue.TokenValueClock, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_REMOVE_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_ON_NETWORK_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TEXT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_VALUES_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    title: str
    time_to_remove: float
    visible_on_network: bool
    template: _templateIdentification_pb2.TemplateIdentification
    clear_type: Message.ClearType
    message_text: str
    tokens: _containers.RepeatedCompositeFieldContainer[Message.Token]
    token_values: _containers.RepeatedCompositeFieldContainer[Message.TokenValue]
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., title: _Optional[str] = ..., time_to_remove: _Optional[float] = ..., visible_on_network: bool = ..., template: _Optional[_Union[_templateIdentification_pb2.TemplateIdentification, _Mapping]] = ..., clear_type: _Optional[_Union[Message.ClearType, str]] = ..., message_text: _Optional[str] = ..., tokens: _Optional[_Iterable[_Union[Message.Token, _Mapping]]] = ..., token_values: _Optional[_Iterable[_Union[Message.TokenValue, _Mapping]]] = ...) -> None: ...

class MessageDocument(_message.Message):
    __slots__ = ("application_info", "messages")
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    application_info: _basicTypes_pb2.ApplicationInfo
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    def __init__(self, application_info: _Optional[_Union[_basicTypes_pb2.ApplicationInfo, _Mapping]] = ..., messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ...) -> None: ...
