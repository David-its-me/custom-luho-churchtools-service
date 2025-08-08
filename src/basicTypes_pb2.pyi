from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class URL(_message.Message):
    __slots__ = ("platform", "absolute_string", "relative_path", "local", "external")
    class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLATFORM_UNKNOWN: _ClassVar[URL.Platform]
        PLATFORM_MACOS: _ClassVar[URL.Platform]
        PLATFORM_WIN32: _ClassVar[URL.Platform]
        PLATFORM_WEB: _ClassVar[URL.Platform]
    PLATFORM_UNKNOWN: URL.Platform
    PLATFORM_MACOS: URL.Platform
    PLATFORM_WIN32: URL.Platform
    PLATFORM_WEB: URL.Platform
    class LocalRelativePath(_message.Message):
        __slots__ = ("root", "path")
        class Root(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ROOT_UNKNOWN: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_BOOT_VOLUME: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_HOME: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_DOCUMENTS: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_DOWNLOADS: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_MUSIC: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_PICTURES: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_VIDEOS: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_DESKTOP: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_APP_SUPPORT: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_SHARED: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_SHOW: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_CURRENT_RESOURCE: _ClassVar[URL.LocalRelativePath.Root]
        ROOT_UNKNOWN: URL.LocalRelativePath.Root
        ROOT_BOOT_VOLUME: URL.LocalRelativePath.Root
        ROOT_USER_HOME: URL.LocalRelativePath.Root
        ROOT_USER_DOCUMENTS: URL.LocalRelativePath.Root
        ROOT_USER_DOWNLOADS: URL.LocalRelativePath.Root
        ROOT_USER_MUSIC: URL.LocalRelativePath.Root
        ROOT_USER_PICTURES: URL.LocalRelativePath.Root
        ROOT_USER_VIDEOS: URL.LocalRelativePath.Root
        ROOT_USER_DESKTOP: URL.LocalRelativePath.Root
        ROOT_USER_APP_SUPPORT: URL.LocalRelativePath.Root
        ROOT_SHARED: URL.LocalRelativePath.Root
        ROOT_SHOW: URL.LocalRelativePath.Root
        ROOT_CURRENT_RESOURCE: URL.LocalRelativePath.Root
        ROOT_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        root: URL.LocalRelativePath.Root
        path: str
        def __init__(self, root: _Optional[_Union[URL.LocalRelativePath.Root, str]] = ..., path: _Optional[str] = ...) -> None: ...
    class ExternalRelativePath(_message.Message):
        __slots__ = ("macos", "win32", "path")
        class MacOSExternalVolume(_message.Message):
            __slots__ = ("volume_name",)
            VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
            volume_name: str
            def __init__(self, volume_name: _Optional[str] = ...) -> None: ...
        class Win32ExternalVolume(_message.Message):
            __slots__ = ("drive_letter", "volume_name", "network_share")
            DRIVE_LETTER_FIELD_NUMBER: _ClassVar[int]
            VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
            NETWORK_SHARE_FIELD_NUMBER: _ClassVar[int]
            drive_letter: str
            volume_name: str
            network_share: bool
            def __init__(self, drive_letter: _Optional[str] = ..., volume_name: _Optional[str] = ..., network_share: bool = ...) -> None: ...
        MACOS_FIELD_NUMBER: _ClassVar[int]
        WIN32_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        macos: URL.ExternalRelativePath.MacOSExternalVolume
        win32: URL.ExternalRelativePath.Win32ExternalVolume
        path: str
        def __init__(self, macos: _Optional[_Union[URL.ExternalRelativePath.MacOSExternalVolume, _Mapping]] = ..., win32: _Optional[_Union[URL.ExternalRelativePath.Win32ExternalVolume, _Mapping]] = ..., path: _Optional[str] = ...) -> None: ...
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_STRING_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    platform: URL.Platform
    absolute_string: str
    relative_path: str
    local: URL.LocalRelativePath
    external: URL.ExternalRelativePath
    def __init__(self, platform: _Optional[_Union[URL.Platform, str]] = ..., absolute_string: _Optional[str] = ..., relative_path: _Optional[str] = ..., local: _Optional[_Union[URL.LocalRelativePath, _Mapping]] = ..., external: _Optional[_Union[URL.ExternalRelativePath, _Mapping]] = ...) -> None: ...

class URLs(_message.Message):
    __slots__ = ("urls",)
    URLS_FIELD_NUMBER: _ClassVar[int]
    urls: _containers.RepeatedCompositeFieldContainer[URL]
    def __init__(self, urls: _Optional[_Iterable[_Union[URL, _Mapping]]] = ...) -> None: ...

class UUID(_message.Message):
    __slots__ = ("string",)
    STRING_FIELD_NUMBER: _ClassVar[int]
    string: str
    def __init__(self, string: _Optional[str] = ...) -> None: ...

class IntRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class Color(_message.Message):
    __slots__ = ("red", "green", "blue", "alpha")
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    red: float
    green: float
    blue: float
    alpha: float
    def __init__(self, red: _Optional[float] = ..., green: _Optional[float] = ..., blue: _Optional[float] = ..., alpha: _Optional[float] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ("major_version", "minor_version", "patch_version", "build")
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PATCH_VERSION_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    major_version: int
    minor_version: int
    patch_version: int
    build: str
    def __init__(self, major_version: _Optional[int] = ..., minor_version: _Optional[int] = ..., patch_version: _Optional[int] = ..., build: _Optional[str] = ...) -> None: ...

class ApplicationInfo(_message.Message):
    __slots__ = ("platform", "platform_version", "application", "application_version")
    class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLATFORM_UNDEFINED: _ClassVar[ApplicationInfo.Platform]
        PLATFORM_MACOS: _ClassVar[ApplicationInfo.Platform]
        PLATFORM_WINDOWS: _ClassVar[ApplicationInfo.Platform]
    PLATFORM_UNDEFINED: ApplicationInfo.Platform
    PLATFORM_MACOS: ApplicationInfo.Platform
    PLATFORM_WINDOWS: ApplicationInfo.Platform
    class Application(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        APPLICATION_UNDEFINED: _ClassVar[ApplicationInfo.Application]
        APPLICATION_PROPRESENTER: _ClassVar[ApplicationInfo.Application]
        APPLICATION_PVP: _ClassVar[ApplicationInfo.Application]
        APPLICATION_PROVIDEOSERVER: _ClassVar[ApplicationInfo.Application]
        APPLICATION_SCOREBOARD: _ClassVar[ApplicationInfo.Application]
    APPLICATION_UNDEFINED: ApplicationInfo.Application
    APPLICATION_PROPRESENTER: ApplicationInfo.Application
    APPLICATION_PVP: ApplicationInfo.Application
    APPLICATION_PROVIDEOSERVER: ApplicationInfo.Application
    APPLICATION_SCOREBOARD: ApplicationInfo.Application
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_VERSION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    platform: ApplicationInfo.Platform
    platform_version: Version
    application: ApplicationInfo.Application
    application_version: Version
    def __init__(self, platform: _Optional[_Union[ApplicationInfo.Platform, str]] = ..., platform_version: _Optional[_Union[Version, _Mapping]] = ..., application: _Optional[_Union[ApplicationInfo.Application, str]] = ..., application_version: _Optional[_Union[Version, _Mapping]] = ...) -> None: ...

class CollectionElementType(_message.Message):
    __slots__ = ("parameter_uuid", "parameter_name")
    PARAMETER_UUID_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    parameter_uuid: UUID
    parameter_name: str
    def __init__(self, parameter_uuid: _Optional[_Union[UUID, _Mapping]] = ..., parameter_name: _Optional[str] = ...) -> None: ...

class MusicKeyScale(_message.Message):
    __slots__ = ("music_key", "music_scale")
    class MusicKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUSIC_KEY_A_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_A: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_A_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_B_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_B: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_B_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_C_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_C: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_C_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_D_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_D: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_D_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_E_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_E: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_E_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_F_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_F: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_F_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_G_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_G: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_G_SHARP: _ClassVar[MusicKeyScale.MusicKey]
    MUSIC_KEY_A_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_A: MusicKeyScale.MusicKey
    MUSIC_KEY_A_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_B_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_B: MusicKeyScale.MusicKey
    MUSIC_KEY_B_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_C_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_C: MusicKeyScale.MusicKey
    MUSIC_KEY_C_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_D_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_D: MusicKeyScale.MusicKey
    MUSIC_KEY_D_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_E_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_E: MusicKeyScale.MusicKey
    MUSIC_KEY_E_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_F_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_F: MusicKeyScale.MusicKey
    MUSIC_KEY_F_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_G_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_G: MusicKeyScale.MusicKey
    MUSIC_KEY_G_SHARP: MusicKeyScale.MusicKey
    class MusicScale(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUSIC_SCALE_MAJOR: _ClassVar[MusicKeyScale.MusicScale]
        MUSIC_SCALE_MINOR: _ClassVar[MusicKeyScale.MusicScale]
    MUSIC_SCALE_MAJOR: MusicKeyScale.MusicScale
    MUSIC_SCALE_MINOR: MusicKeyScale.MusicScale
    MUSIC_KEY_FIELD_NUMBER: _ClassVar[int]
    MUSIC_SCALE_FIELD_NUMBER: _ClassVar[int]
    music_key: MusicKeyScale.MusicKey
    music_scale: MusicKeyScale.MusicScale
    def __init__(self, music_key: _Optional[_Union[MusicKeyScale.MusicKey, str]] = ..., music_scale: _Optional[_Union[MusicKeyScale.MusicScale, str]] = ...) -> None: ...
