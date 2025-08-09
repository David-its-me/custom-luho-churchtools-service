import propresenter.pb_auto_generated.proscreen_pb2 as _proscreen_pb2
import propresenter.pb_auto_generated.proAudienceLook_pb2 as _proAudienceLook_pb2
import propresenter.pb_auto_generated.proMask_pb2 as _proMask_pb2
import propresenter.pb_auto_generated.input_pb2 as _input_pb2
import propresenter.pb_auto_generated.audio_pb2 as _audio_pb2
import propresenter.pb_auto_generated.digitalAudio_pb2 as _digitalAudio_pb2
import propresenter.pb_auto_generated.stage_pb2 as _stage_pb2
import propresenter.pb_auto_generated.recording_pb2 as _recording_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProPresenterWorkspace(_message.Message):
    __slots__ = ("pro_screens", "audience_looks", "live_audience_look", "masks", "videoInputs", "stage_layout_mappings", "audio_settings", "selected_library_name", "record_settings", "digital_audio_setup", "audio_inputs", "audio_input_transition_time")
    PRO_SCREENS_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_LOOKS_FIELD_NUMBER: _ClassVar[int]
    LIVE_AUDIENCE_LOOK_FIELD_NUMBER: _ClassVar[int]
    MASKS_FIELD_NUMBER: _ClassVar[int]
    VIDEOINPUTS_FIELD_NUMBER: _ClassVar[int]
    STAGE_LAYOUT_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_LIBRARY_NAME_FIELD_NUMBER: _ClassVar[int]
    RECORD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_AUDIO_SETUP_FIELD_NUMBER: _ClassVar[int]
    AUDIO_INPUTS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_INPUT_TRANSITION_TIME_FIELD_NUMBER: _ClassVar[int]
    pro_screens: _containers.RepeatedCompositeFieldContainer[_proscreen_pb2.ProPresenterScreen]
    audience_looks: _containers.RepeatedCompositeFieldContainer[_proAudienceLook_pb2.ProAudienceLook]
    live_audience_look: _proAudienceLook_pb2.ProAudienceLook
    masks: _containers.RepeatedCompositeFieldContainer[_proMask_pb2.ProMask]
    videoInputs: _containers.RepeatedCompositeFieldContainer[_input_pb2.VideoInput]
    stage_layout_mappings: _containers.RepeatedCompositeFieldContainer[_stage_pb2.Stage.ScreenAssignment]
    audio_settings: _audio_pb2.Audio.SettingsDocument
    selected_library_name: str
    record_settings: _recording_pb2.Recording.SettingsDocument
    digital_audio_setup: _digitalAudio_pb2.DigitalAudio.Setup
    audio_inputs: _containers.RepeatedCompositeFieldContainer[_input_pb2.AudioInput]
    audio_input_transition_time: float
    def __init__(self, pro_screens: _Optional[_Iterable[_Union[_proscreen_pb2.ProPresenterScreen, _Mapping]]] = ..., audience_looks: _Optional[_Iterable[_Union[_proAudienceLook_pb2.ProAudienceLook, _Mapping]]] = ..., live_audience_look: _Optional[_Union[_proAudienceLook_pb2.ProAudienceLook, _Mapping]] = ..., masks: _Optional[_Iterable[_Union[_proMask_pb2.ProMask, _Mapping]]] = ..., videoInputs: _Optional[_Iterable[_Union[_input_pb2.VideoInput, _Mapping]]] = ..., stage_layout_mappings: _Optional[_Iterable[_Union[_stage_pb2.Stage.ScreenAssignment, _Mapping]]] = ..., audio_settings: _Optional[_Union[_audio_pb2.Audio.SettingsDocument, _Mapping]] = ..., selected_library_name: _Optional[str] = ..., record_settings: _Optional[_Union[_recording_pb2.Recording.SettingsDocument, _Mapping]] = ..., digital_audio_setup: _Optional[_Union[_digitalAudio_pb2.DigitalAudio.Setup, _Mapping]] = ..., audio_inputs: _Optional[_Iterable[_Union[_input_pb2.AudioInput, _Mapping]]] = ..., audio_input_transition_time: _Optional[float] = ...) -> None: ...
