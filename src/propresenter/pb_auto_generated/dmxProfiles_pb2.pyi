from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DMXProfiles(_message.Message):
    __slots__ = ("workspaceProfile", "layerProfiles")
    class DMXProfile(_message.Message):
        __slots__ = ("profile", "fixture", "isEnabled", "customMappings")
        class Profile(_message.Message):
            __slots__ = ("profileType", "startingChannel")
            class ProfileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                BASIC: _ClassVar[DMXProfiles.DMXProfile.Profile.ProfileType]
                ADVANCED: _ClassVar[DMXProfiles.DMXProfile.Profile.ProfileType]
                CUSTOM: _ClassVar[DMXProfiles.DMXProfile.Profile.ProfileType]
            BASIC: DMXProfiles.DMXProfile.Profile.ProfileType
            ADVANCED: DMXProfiles.DMXProfile.Profile.ProfileType
            CUSTOM: DMXProfiles.DMXProfile.Profile.ProfileType
            PROFILETYPE_FIELD_NUMBER: _ClassVar[int]
            STARTINGCHANNEL_FIELD_NUMBER: _ClassVar[int]
            profileType: DMXProfiles.DMXProfile.Profile.ProfileType
            startingChannel: int
            def __init__(self, profileType: _Optional[_Union[DMXProfiles.DMXProfile.Profile.ProfileType, str]] = ..., startingChannel: _Optional[int] = ...) -> None: ...
        class ChannelMapping(_message.Message):
            __slots__ = ("channelIndex", "command")
            class CommandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                OPACITY: _ClassVar[DMXProfiles.DMXProfile.ChannelMapping.CommandType]
                BLEND_MODE: _ClassVar[DMXProfiles.DMXProfile.ChannelMapping.CommandType]
                SELECT_CUE: _ClassVar[DMXProfiles.DMXProfile.ChannelMapping.CommandType]
                CONTROL_TYPE: _ClassVar[DMXProfiles.DMXProfile.ChannelMapping.CommandType]
                CONTROL_VALUE: _ClassVar[DMXProfiles.DMXProfile.ChannelMapping.CommandType]
                TRANSITION_DURATION: _ClassVar[DMXProfiles.DMXProfile.ChannelMapping.CommandType]
                SELECT_PLAYLIST: _ClassVar[DMXProfiles.DMXProfile.ChannelMapping.CommandType]
                TARGETED_LAYER: _ClassVar[DMXProfiles.DMXProfile.ChannelMapping.CommandType]
            OPACITY: DMXProfiles.DMXProfile.ChannelMapping.CommandType
            BLEND_MODE: DMXProfiles.DMXProfile.ChannelMapping.CommandType
            SELECT_CUE: DMXProfiles.DMXProfile.ChannelMapping.CommandType
            CONTROL_TYPE: DMXProfiles.DMXProfile.ChannelMapping.CommandType
            CONTROL_VALUE: DMXProfiles.DMXProfile.ChannelMapping.CommandType
            TRANSITION_DURATION: DMXProfiles.DMXProfile.ChannelMapping.CommandType
            SELECT_PLAYLIST: DMXProfiles.DMXProfile.ChannelMapping.CommandType
            TARGETED_LAYER: DMXProfiles.DMXProfile.ChannelMapping.CommandType
            CHANNELINDEX_FIELD_NUMBER: _ClassVar[int]
            COMMAND_FIELD_NUMBER: _ClassVar[int]
            channelIndex: int
            command: DMXProfiles.DMXProfile.ChannelMapping.CommandType
            def __init__(self, channelIndex: _Optional[int] = ..., command: _Optional[_Union[DMXProfiles.DMXProfile.ChannelMapping.CommandType, str]] = ...) -> None: ...
        class Fixture(_message.Message):
            __slots__ = ("fixtureType", "layerIndex")
            class FixtureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                WORKSPACE: _ClassVar[DMXProfiles.DMXProfile.Fixture.FixtureType]
                LAYER: _ClassVar[DMXProfiles.DMXProfile.Fixture.FixtureType]
            WORKSPACE: DMXProfiles.DMXProfile.Fixture.FixtureType
            LAYER: DMXProfiles.DMXProfile.Fixture.FixtureType
            FIXTURETYPE_FIELD_NUMBER: _ClassVar[int]
            LAYERINDEX_FIELD_NUMBER: _ClassVar[int]
            fixtureType: DMXProfiles.DMXProfile.Fixture.FixtureType
            layerIndex: int
            def __init__(self, fixtureType: _Optional[_Union[DMXProfiles.DMXProfile.Fixture.FixtureType, str]] = ..., layerIndex: _Optional[int] = ...) -> None: ...
        PROFILE_FIELD_NUMBER: _ClassVar[int]
        FIXTURE_FIELD_NUMBER: _ClassVar[int]
        ISENABLED_FIELD_NUMBER: _ClassVar[int]
        CUSTOMMAPPINGS_FIELD_NUMBER: _ClassVar[int]
        profile: DMXProfiles.DMXProfile.Profile
        fixture: DMXProfiles.DMXProfile.Fixture
        isEnabled: bool
        customMappings: _containers.RepeatedCompositeFieldContainer[DMXProfiles.DMXProfile.ChannelMapping]
        def __init__(self, profile: _Optional[_Union[DMXProfiles.DMXProfile.Profile, _Mapping]] = ..., fixture: _Optional[_Union[DMXProfiles.DMXProfile.Fixture, _Mapping]] = ..., isEnabled: bool = ..., customMappings: _Optional[_Iterable[_Union[DMXProfiles.DMXProfile.ChannelMapping, _Mapping]]] = ...) -> None: ...
    WORKSPACEPROFILE_FIELD_NUMBER: _ClassVar[int]
    LAYERPROFILES_FIELD_NUMBER: _ClassVar[int]
    workspaceProfile: DMXProfiles.DMXProfile
    layerProfiles: _containers.RepeatedCompositeFieldContainer[DMXProfiles.DMXProfile]
    def __init__(self, workspaceProfile: _Optional[_Union[DMXProfiles.DMXProfile, _Mapping]] = ..., layerProfiles: _Optional[_Iterable[_Union[DMXProfiles.DMXProfile, _Mapping]]] = ...) -> None: ...
