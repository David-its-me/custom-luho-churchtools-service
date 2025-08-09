import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.messages_pb2 as _messages_pb2
import propresenter.pb_auto_generated.timers_pb2 as _timers_pb2
import propresenter.pb_auto_generated.rvtimestamp_pb2 as _rvtimestamp_pb2
import propresenter.pb_auto_generated.proApiV1_pb2 as _proApiV1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProApiIn(_message.Message):
    __slots__ = ("handler_in", "network_api", "network_api_v1")
    HANDLER_IN_FIELD_NUMBER: _ClassVar[int]
    NETWORK_API_FIELD_NUMBER: _ClassVar[int]
    NETWORK_API_V1_FIELD_NUMBER: _ClassVar[int]
    handler_in: ProLink.HandlerIn
    network_api: NetworkAPI
    network_api_v1: _proApiV1_pb2.NetworkAPI_v1
    def __init__(self, handler_in: _Optional[_Union[ProLink.HandlerIn, _Mapping]] = ..., network_api: _Optional[_Union[NetworkAPI, _Mapping]] = ..., network_api_v1: _Optional[_Union[_proApiV1_pb2.NetworkAPI_v1, _Mapping]] = ...) -> None: ...

class ProApiOut(_message.Message):
    __slots__ = ("handler_out", "client_action", "network_api", "network_api_v1")
    HANDLER_OUT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ACTION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_API_FIELD_NUMBER: _ClassVar[int]
    NETWORK_API_V1_FIELD_NUMBER: _ClassVar[int]
    handler_out: ProLink.HandlerOut
    client_action: ProLink.ClientAction
    network_api: NetworkAPI
    network_api_v1: _proApiV1_pb2.NetworkAPI_v1
    def __init__(self, handler_out: _Optional[_Union[ProLink.HandlerOut, _Mapping]] = ..., client_action: _Optional[_Union[ProLink.ClientAction, _Mapping]] = ..., network_api: _Optional[_Union[NetworkAPI, _Mapping]] = ..., network_api_v1: _Optional[_Union[_proApiV1_pb2.NetworkAPI_v1, _Mapping]] = ...) -> None: ...

class ProApiNetworkConfiguration(_message.Message):
    __slots__ = ("enable_network", "port", "network_name", "remote_enable", "remote_control_enable", "remote_control_password", "remote_observe_enable", "remote_observe_password", "stage_enable", "stage_password", "link_enable", "web_resource_root")
    ENABLE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ENABLE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CONTROL_ENABLE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CONTROL_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    REMOTE_OBSERVE_ENABLE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_OBSERVE_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    STAGE_ENABLE_FIELD_NUMBER: _ClassVar[int]
    STAGE_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    LINK_ENABLE_FIELD_NUMBER: _ClassVar[int]
    WEB_RESOURCE_ROOT_FIELD_NUMBER: _ClassVar[int]
    enable_network: bool
    port: int
    network_name: str
    remote_enable: bool
    remote_control_enable: bool
    remote_control_password: str
    remote_observe_enable: bool
    remote_observe_password: str
    stage_enable: bool
    stage_password: str
    link_enable: bool
    web_resource_root: str
    def __init__(self, enable_network: bool = ..., port: _Optional[int] = ..., network_name: _Optional[str] = ..., remote_enable: bool = ..., remote_control_enable: bool = ..., remote_control_password: _Optional[str] = ..., remote_observe_enable: bool = ..., remote_observe_password: _Optional[str] = ..., stage_enable: bool = ..., stage_password: _Optional[str] = ..., link_enable: bool = ..., web_resource_root: _Optional[str] = ...) -> None: ...

class ProLink(_message.Message):
    __slots__ = ()
    class GroupDefinition(_message.Message):
        __slots__ = ("timestamp", "secret", "name", "members", "group_identifier")
        class Member(_message.Message):
            __slots__ = ("ip", "port")
            IP_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            ip: str
            port: int
            def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SECRET_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        MEMBERS_FIELD_NUMBER: _ClassVar[int]
        GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        timestamp: _rvtimestamp_pb2.Timestamp
        secret: str
        name: str
        members: _containers.RepeatedCompositeFieldContainer[ProLink.GroupDefinition.Member]
        group_identifier: _basicTypes_pb2.UUID
        def __init__(self, timestamp: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., secret: _Optional[str] = ..., name: _Optional[str] = ..., members: _Optional[_Iterable[_Union[ProLink.GroupDefinition.Member, _Mapping]]] = ..., group_identifier: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
    class ZeroConfig(_message.Message):
        __slots__ = ()
        class NetworkEnvironment(_message.Message):
            __slots__ = ("available_groups", "available_devices")
            AVAILABLE_GROUPS_FIELD_NUMBER: _ClassVar[int]
            AVAILABLE_DEVICES_FIELD_NUMBER: _ClassVar[int]
            available_groups: _containers.RepeatedCompositeFieldContainer[ProLink.GroupDefinition]
            available_devices: _containers.RepeatedCompositeFieldContainer[ProLink.MemberStatus]
            def __init__(self, available_groups: _Optional[_Iterable[_Union[ProLink.GroupDefinition, _Mapping]]] = ..., available_devices: _Optional[_Iterable[_Union[ProLink.MemberStatus, _Mapping]]] = ...) -> None: ...
        class MulticastPacket(_message.Message):
            __slots__ = ("group", "device")
            GROUP_FIELD_NUMBER: _ClassVar[int]
            DEVICE_FIELD_NUMBER: _ClassVar[int]
            group: ProLink.GroupDefinition
            device: ProLink.MemberStatus
            def __init__(self, group: _Optional[_Union[ProLink.GroupDefinition, _Mapping]] = ..., device: _Optional[_Union[ProLink.MemberStatus, _Mapping]] = ...) -> None: ...
        def __init__(self) -> None: ...
    class TowerMessage(_message.Message):
        __slots__ = ()
        class TowerStatusRequest(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TowerStatusResponse(_message.Message):
            __slots__ = ("member_name", "group_definition")
            MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
            GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            member_name: str
            group_definition: ProLink.GroupDefinition
            def __init__(self, member_name: _Optional[str] = ..., group_definition: _Optional[_Union[ProLink.GroupDefinition, _Mapping]] = ...) -> None: ...
        class TowerAddMemberRequest(_message.Message):
            __slots__ = ("group_definition", "joining_member")
            GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            JOINING_MEMBER_FIELD_NUMBER: _ClassVar[int]
            group_definition: ProLink.GroupDefinition
            joining_member: ProLink.GroupDefinition.Member
            def __init__(self, group_definition: _Optional[_Union[ProLink.GroupDefinition, _Mapping]] = ..., joining_member: _Optional[_Union[ProLink.GroupDefinition.Member, _Mapping]] = ...) -> None: ...
        class TowerRemoveMemberRequest(_message.Message):
            __slots__ = ("removing_member",)
            REMOVING_MEMBER_FIELD_NUMBER: _ClassVar[int]
            removing_member: ProLink.GroupDefinition.Member
            def __init__(self, removing_member: _Optional[_Union[ProLink.GroupDefinition.Member, _Mapping]] = ...) -> None: ...
        class TowerAddMemberResponse(_message.Message):
            __slots__ = ("group_definition", "accept", "decline_reason")
            class DeclineReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ALREADY_IN_GROUP: _ClassVar[ProLink.TowerMessage.TowerAddMemberResponse.DeclineReason]
                USER_DECLINED: _ClassVar[ProLink.TowerMessage.TowerAddMemberResponse.DeclineReason]
            ALREADY_IN_GROUP: ProLink.TowerMessage.TowerAddMemberResponse.DeclineReason
            USER_DECLINED: ProLink.TowerMessage.TowerAddMemberResponse.DeclineReason
            class Accept(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            ACCEPT_FIELD_NUMBER: _ClassVar[int]
            DECLINE_REASON_FIELD_NUMBER: _ClassVar[int]
            group_definition: ProLink.GroupDefinition
            accept: ProLink.TowerMessage.TowerAddMemberResponse.Accept
            decline_reason: ProLink.TowerMessage.TowerAddMemberResponse.DeclineReason
            def __init__(self, group_definition: _Optional[_Union[ProLink.GroupDefinition, _Mapping]] = ..., accept: _Optional[_Union[ProLink.TowerMessage.TowerAddMemberResponse.Accept, _Mapping]] = ..., decline_reason: _Optional[_Union[ProLink.TowerMessage.TowerAddMemberResponse.DeclineReason, str]] = ...) -> None: ...
        class TowerHeartbeatRequest(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TowerHeartbeatResponse(_message.Message):
            __slots__ = ("group_definition",)
            GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            group_definition: ProLink.GroupDefinition
            def __init__(self, group_definition: _Optional[_Union[ProLink.GroupDefinition, _Mapping]] = ...) -> None: ...
        def __init__(self) -> None: ...
    class MemberStatus(_message.Message):
        __slots__ = ("ip", "port", "name", "platform", "os_version", "host_description", "api_version", "connection_status")
        class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PLATFORM_UNDEFINED: _ClassVar[ProLink.MemberStatus.Platform]
            PLATFORM_MACOS: _ClassVar[ProLink.MemberStatus.Platform]
            PLATFORM_WINDOWS: _ClassVar[ProLink.MemberStatus.Platform]
        PLATFORM_UNDEFINED: ProLink.MemberStatus.Platform
        PLATFORM_MACOS: ProLink.MemberStatus.Platform
        PLATFORM_WINDOWS: ProLink.MemberStatus.Platform
        class ConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONNECTION_STATUS_UNKNOWN: _ClassVar[ProLink.MemberStatus.ConnectionStatus]
            CONNECTION_STATUS_CONNECTED: _ClassVar[ProLink.MemberStatus.ConnectionStatus]
            CONNECTION_STATUS_DISCONNECTED: _ClassVar[ProLink.MemberStatus.ConnectionStatus]
        CONNECTION_STATUS_UNKNOWN: ProLink.MemberStatus.ConnectionStatus
        CONNECTION_STATUS_CONNECTED: ProLink.MemberStatus.ConnectionStatus
        CONNECTION_STATUS_DISCONNECTED: ProLink.MemberStatus.ConnectionStatus
        IP_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        HOST_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        API_VERSION_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
        ip: str
        port: int
        name: str
        platform: ProLink.MemberStatus.Platform
        os_version: str
        host_description: str
        api_version: str
        connection_status: ProLink.MemberStatus.ConnectionStatus
        def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., name: _Optional[str] = ..., platform: _Optional[_Union[ProLink.MemberStatus.Platform, str]] = ..., os_version: _Optional[str] = ..., host_description: _Optional[str] = ..., api_version: _Optional[str] = ..., connection_status: _Optional[_Union[ProLink.MemberStatus.ConnectionStatus, str]] = ...) -> None: ...
    class ClientAction(_message.Message):
        __slots__ = ("add_connection", "remove_connection", "cancel_action", "render_time")
        class AddConnection(_message.Message):
            __slots__ = ("ip", "port", "group_name")
            IP_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            ip: str
            port: int
            group_name: str
            def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., group_name: _Optional[str] = ...) -> None: ...
        class RemoveConnection(_message.Message):
            __slots__ = ("ip", "port")
            IP_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            ip: str
            port: int
            def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...
        class CancelAction(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class RenderTime(_message.Message):
            __slots__ = ("latency", "render_time")
            LATENCY_FIELD_NUMBER: _ClassVar[int]
            RENDER_TIME_FIELD_NUMBER: _ClassVar[int]
            latency: int
            render_time: int
            def __init__(self, latency: _Optional[int] = ..., render_time: _Optional[int] = ...) -> None: ...
        ADD_CONNECTION_FIELD_NUMBER: _ClassVar[int]
        REMOVE_CONNECTION_FIELD_NUMBER: _ClassVar[int]
        CANCEL_ACTION_FIELD_NUMBER: _ClassVar[int]
        RENDER_TIME_FIELD_NUMBER: _ClassVar[int]
        add_connection: ProLink.ClientAction.AddConnection
        remove_connection: ProLink.ClientAction.RemoveConnection
        cancel_action: ProLink.ClientAction.CancelAction
        render_time: ProLink.ClientAction.RenderTime
        def __init__(self, add_connection: _Optional[_Union[ProLink.ClientAction.AddConnection, _Mapping]] = ..., remove_connection: _Optional[_Union[ProLink.ClientAction.RemoveConnection, _Mapping]] = ..., cancel_action: _Optional[_Union[ProLink.ClientAction.CancelAction, _Mapping]] = ..., render_time: _Optional[_Union[ProLink.ClientAction.RenderTime, _Mapping]] = ...) -> None: ...
    class HandlerIn(_message.Message):
        __slots__ = ("group_name", "group_definition_request", "group_join_confirmation", "group_join_password", "add_connection_result", "group_update", "member_status_change", "propresenter_info", "server_state", "configuration_request", "zeroconfig_network_environment_change", "log_request")
        class GroupName(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GroupDefinitionRequest(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GroupJoinConfirmation(_message.Message):
            __slots__ = ("name",)
            NAME_FIELD_NUMBER: _ClassVar[int]
            name: str
            def __init__(self, name: _Optional[str] = ...) -> None: ...
        class GroupJoinPassword(_message.Message):
            __slots__ = ("name",)
            NAME_FIELD_NUMBER: _ClassVar[int]
            name: str
            def __init__(self, name: _Optional[str] = ...) -> None: ...
        class AddConnectionResult(_message.Message):
            __slots__ = ("success", "failure")
            class Success(_message.Message):
                __slots__ = ("new_group_definition",)
                NEW_GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
                new_group_definition: ProLink.GroupDefinition
                def __init__(self, new_group_definition: _Optional[_Union[ProLink.GroupDefinition, _Mapping]] = ...) -> None: ...
            class Failure(_message.Message):
                __slots__ = ("unexpected", "declined", "timeout", "link_disabled", "in_other_group", "invalid_ip_address", "already_in_group", "could_not_add", "could_not_join")
                class Unexpected(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class Declined(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class Timeout(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class LinkDisabled(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class InOtherGroup(_message.Message):
                    __slots__ = ("member_name", "group_name")
                    MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
                    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
                    member_name: str
                    group_name: str
                    def __init__(self, member_name: _Optional[str] = ..., group_name: _Optional[str] = ...) -> None: ...
                class InvalidIpAddress(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class AlreadyInGroup(_message.Message):
                    __slots__ = ("member_name", "group_name")
                    MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
                    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
                    member_name: str
                    group_name: str
                    def __init__(self, member_name: _Optional[str] = ..., group_name: _Optional[str] = ...) -> None: ...
                class CouldNotAdd(_message.Message):
                    __slots__ = ("member_name",)
                    MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
                    member_name: str
                    def __init__(self, member_name: _Optional[str] = ...) -> None: ...
                class CouldNotJoin(_message.Message):
                    __slots__ = ("group_name",)
                    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
                    group_name: str
                    def __init__(self, group_name: _Optional[str] = ...) -> None: ...
                UNEXPECTED_FIELD_NUMBER: _ClassVar[int]
                DECLINED_FIELD_NUMBER: _ClassVar[int]
                TIMEOUT_FIELD_NUMBER: _ClassVar[int]
                LINK_DISABLED_FIELD_NUMBER: _ClassVar[int]
                IN_OTHER_GROUP_FIELD_NUMBER: _ClassVar[int]
                INVALID_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
                ALREADY_IN_GROUP_FIELD_NUMBER: _ClassVar[int]
                COULD_NOT_ADD_FIELD_NUMBER: _ClassVar[int]
                COULD_NOT_JOIN_FIELD_NUMBER: _ClassVar[int]
                unexpected: ProLink.HandlerIn.AddConnectionResult.Failure.Unexpected
                declined: ProLink.HandlerIn.AddConnectionResult.Failure.Declined
                timeout: ProLink.HandlerIn.AddConnectionResult.Failure.Timeout
                link_disabled: ProLink.HandlerIn.AddConnectionResult.Failure.LinkDisabled
                in_other_group: ProLink.HandlerIn.AddConnectionResult.Failure.InOtherGroup
                invalid_ip_address: ProLink.HandlerIn.AddConnectionResult.Failure.InvalidIpAddress
                already_in_group: ProLink.HandlerIn.AddConnectionResult.Failure.AlreadyInGroup
                could_not_add: ProLink.HandlerIn.AddConnectionResult.Failure.CouldNotAdd
                could_not_join: ProLink.HandlerIn.AddConnectionResult.Failure.CouldNotJoin
                def __init__(self, unexpected: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Failure.Unexpected, _Mapping]] = ..., declined: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Failure.Declined, _Mapping]] = ..., timeout: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Failure.Timeout, _Mapping]] = ..., link_disabled: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Failure.LinkDisabled, _Mapping]] = ..., in_other_group: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Failure.InOtherGroup, _Mapping]] = ..., invalid_ip_address: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Failure.InvalidIpAddress, _Mapping]] = ..., already_in_group: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Failure.AlreadyInGroup, _Mapping]] = ..., could_not_add: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Failure.CouldNotAdd, _Mapping]] = ..., could_not_join: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Failure.CouldNotJoin, _Mapping]] = ...) -> None: ...
            SUCCESS_FIELD_NUMBER: _ClassVar[int]
            FAILURE_FIELD_NUMBER: _ClassVar[int]
            success: ProLink.HandlerIn.AddConnectionResult.Success
            failure: ProLink.HandlerIn.AddConnectionResult.Failure
            def __init__(self, success: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Success, _Mapping]] = ..., failure: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult.Failure, _Mapping]] = ...) -> None: ...
        class MemberStatusChange(_message.Message):
            __slots__ = ("members",)
            MEMBERS_FIELD_NUMBER: _ClassVar[int]
            members: _containers.RepeatedCompositeFieldContainer[ProLink.MemberStatus]
            def __init__(self, members: _Optional[_Iterable[_Union[ProLink.MemberStatus, _Mapping]]] = ...) -> None: ...
        class ProPresenterInfo(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ServerState(_message.Message):
            __slots__ = ("local_ip", "public_ip", "port", "success")
            LOCAL_IP_FIELD_NUMBER: _ClassVar[int]
            PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            SUCCESS_FIELD_NUMBER: _ClassVar[int]
            local_ip: str
            public_ip: str
            port: int
            success: bool
            def __init__(self, local_ip: _Optional[str] = ..., public_ip: _Optional[str] = ..., port: _Optional[int] = ..., success: bool = ...) -> None: ...
        class ConfigurationRequest(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class LogRequest(_message.Message):
            __slots__ = ("severity", "message")
            class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SEVERITY_DEBUG: _ClassVar[ProLink.HandlerIn.LogRequest.Severity]
                SEVERITY_DEBUG_WARNING: _ClassVar[ProLink.HandlerIn.LogRequest.Severity]
                SEVERITY_INFO: _ClassVar[ProLink.HandlerIn.LogRequest.Severity]
                SEVERITY_WARNING: _ClassVar[ProLink.HandlerIn.LogRequest.Severity]
                SEVERITY_ERROR: _ClassVar[ProLink.HandlerIn.LogRequest.Severity]
                SEVERITY_FATAL_ERROR: _ClassVar[ProLink.HandlerIn.LogRequest.Severity]
            SEVERITY_DEBUG: ProLink.HandlerIn.LogRequest.Severity
            SEVERITY_DEBUG_WARNING: ProLink.HandlerIn.LogRequest.Severity
            SEVERITY_INFO: ProLink.HandlerIn.LogRequest.Severity
            SEVERITY_WARNING: ProLink.HandlerIn.LogRequest.Severity
            SEVERITY_ERROR: ProLink.HandlerIn.LogRequest.Severity
            SEVERITY_FATAL_ERROR: ProLink.HandlerIn.LogRequest.Severity
            SEVERITY_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            severity: ProLink.HandlerIn.LogRequest.Severity
            message: str
            def __init__(self, severity: _Optional[_Union[ProLink.HandlerIn.LogRequest.Severity, str]] = ..., message: _Optional[str] = ...) -> None: ...
        GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_DEFINITION_REQUEST_FIELD_NUMBER: _ClassVar[int]
        GROUP_JOIN_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
        GROUP_JOIN_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        ADD_CONNECTION_RESULT_FIELD_NUMBER: _ClassVar[int]
        GROUP_UPDATE_FIELD_NUMBER: _ClassVar[int]
        MEMBER_STATUS_CHANGE_FIELD_NUMBER: _ClassVar[int]
        PROPRESENTER_INFO_FIELD_NUMBER: _ClassVar[int]
        SERVER_STATE_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
        ZEROCONFIG_NETWORK_ENVIRONMENT_CHANGE_FIELD_NUMBER: _ClassVar[int]
        LOG_REQUEST_FIELD_NUMBER: _ClassVar[int]
        group_name: ProLink.HandlerIn.GroupName
        group_definition_request: ProLink.HandlerIn.GroupDefinitionRequest
        group_join_confirmation: ProLink.HandlerIn.GroupJoinConfirmation
        group_join_password: ProLink.HandlerIn.GroupJoinPassword
        add_connection_result: ProLink.HandlerIn.AddConnectionResult
        group_update: ProLink.GroupDefinition
        member_status_change: ProLink.HandlerIn.MemberStatusChange
        propresenter_info: ProLink.HandlerIn.ProPresenterInfo
        server_state: ProLink.HandlerIn.ServerState
        configuration_request: ProLink.HandlerIn.ConfigurationRequest
        zeroconfig_network_environment_change: ProLink.ZeroConfig.NetworkEnvironment
        log_request: ProLink.HandlerIn.LogRequest
        def __init__(self, group_name: _Optional[_Union[ProLink.HandlerIn.GroupName, _Mapping]] = ..., group_definition_request: _Optional[_Union[ProLink.HandlerIn.GroupDefinitionRequest, _Mapping]] = ..., group_join_confirmation: _Optional[_Union[ProLink.HandlerIn.GroupJoinConfirmation, _Mapping]] = ..., group_join_password: _Optional[_Union[ProLink.HandlerIn.GroupJoinPassword, _Mapping]] = ..., add_connection_result: _Optional[_Union[ProLink.HandlerIn.AddConnectionResult, _Mapping]] = ..., group_update: _Optional[_Union[ProLink.GroupDefinition, _Mapping]] = ..., member_status_change: _Optional[_Union[ProLink.HandlerIn.MemberStatusChange, _Mapping]] = ..., propresenter_info: _Optional[_Union[ProLink.HandlerIn.ProPresenterInfo, _Mapping]] = ..., server_state: _Optional[_Union[ProLink.HandlerIn.ServerState, _Mapping]] = ..., configuration_request: _Optional[_Union[ProLink.HandlerIn.ConfigurationRequest, _Mapping]] = ..., zeroconfig_network_environment_change: _Optional[_Union[ProLink.ZeroConfig.NetworkEnvironment, _Mapping]] = ..., log_request: _Optional[_Union[ProLink.HandlerIn.LogRequest, _Mapping]] = ...) -> None: ...
    class HandlerOut(_message.Message):
        __slots__ = ("group_name", "group_definition", "group_join_confirmation", "group_join_password", "propresenter_info", "configuration")
        class GroupName(_message.Message):
            __slots__ = ("name",)
            NAME_FIELD_NUMBER: _ClassVar[int]
            name: str
            def __init__(self, name: _Optional[str] = ...) -> None: ...
        class GroupJoinConfirmation(_message.Message):
            __slots__ = ("accept",)
            ACCEPT_FIELD_NUMBER: _ClassVar[int]
            accept: bool
            def __init__(self, accept: bool = ...) -> None: ...
        class GroupJoinPassword(_message.Message):
            __slots__ = ("password",)
            PASSWORD_FIELD_NUMBER: _ClassVar[int]
            password: str
            def __init__(self, password: _Optional[str] = ...) -> None: ...
        class ProPresenterInfo(_message.Message):
            __slots__ = ("platform", "os_version", "host_description")
            class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PLATFORM_UNDEFINED: _ClassVar[ProLink.HandlerOut.ProPresenterInfo.Platform]
                PLATFORM_MACOS: _ClassVar[ProLink.HandlerOut.ProPresenterInfo.Platform]
                PLATFORM_WINDOWS: _ClassVar[ProLink.HandlerOut.ProPresenterInfo.Platform]
            PLATFORM_UNDEFINED: ProLink.HandlerOut.ProPresenterInfo.Platform
            PLATFORM_MACOS: ProLink.HandlerOut.ProPresenterInfo.Platform
            PLATFORM_WINDOWS: ProLink.HandlerOut.ProPresenterInfo.Platform
            PLATFORM_FIELD_NUMBER: _ClassVar[int]
            OS_VERSION_FIELD_NUMBER: _ClassVar[int]
            HOST_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            platform: ProLink.HandlerOut.ProPresenterInfo.Platform
            os_version: str
            host_description: str
            def __init__(self, platform: _Optional[_Union[ProLink.HandlerOut.ProPresenterInfo.Platform, str]] = ..., os_version: _Optional[str] = ..., host_description: _Optional[str] = ...) -> None: ...
        GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
        GROUP_JOIN_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
        GROUP_JOIN_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        PROPRESENTER_INFO_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        group_name: ProLink.HandlerOut.GroupName
        group_definition: ProLink.GroupDefinition
        group_join_confirmation: ProLink.HandlerOut.GroupJoinConfirmation
        group_join_password: ProLink.HandlerOut.GroupJoinPassword
        propresenter_info: ProLink.HandlerOut.ProPresenterInfo
        configuration: ProApiNetworkConfiguration
        def __init__(self, group_name: _Optional[_Union[ProLink.HandlerOut.GroupName, _Mapping]] = ..., group_definition: _Optional[_Union[ProLink.GroupDefinition, _Mapping]] = ..., group_join_confirmation: _Optional[_Union[ProLink.HandlerOut.GroupJoinConfirmation, _Mapping]] = ..., group_join_password: _Optional[_Union[ProLink.HandlerOut.GroupJoinPassword, _Mapping]] = ..., propresenter_info: _Optional[_Union[ProLink.HandlerOut.ProPresenterInfo, _Mapping]] = ..., configuration: _Optional[_Union[ProApiNetworkConfiguration, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class NetworkAPI(_message.Message):
    __slots__ = ("action", "server_state", "group_change", "group_response")
    class LinkStatus(_message.Message):
        __slots__ = ("platform", "os_version", "version", "description", "group_info")
        class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PLATFORM_UNDEFINED: _ClassVar[NetworkAPI.LinkStatus.Platform]
            PLATFORM_MACOS: _ClassVar[NetworkAPI.LinkStatus.Platform]
            PLATFORM_WINDOWS: _ClassVar[NetworkAPI.LinkStatus.Platform]
        PLATFORM_UNDEFINED: NetworkAPI.LinkStatus.Platform
        PLATFORM_MACOS: NetworkAPI.LinkStatus.Platform
        PLATFORM_WINDOWS: NetworkAPI.LinkStatus.Platform
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
        platform: NetworkAPI.LinkStatus.Platform
        os_version: str
        version: str
        description: str
        group_info: NetworkAPI.Group
        def __init__(self, platform: _Optional[_Union[NetworkAPI.LinkStatus.Platform, str]] = ..., os_version: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., group_info: _Optional[_Union[NetworkAPI.Group, _Mapping]] = ...) -> None: ...
    class Group(_message.Message):
        __slots__ = ("name", "members")
        class Member(_message.Message):
            __slots__ = ("ip_address", "port")
            IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            ip_address: str
            port: int
            def __init__(self, ip_address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        MEMBERS_FIELD_NUMBER: _ClassVar[int]
        name: str
        members: _containers.RepeatedCompositeFieldContainer[NetworkAPI.Group.Member]
        def __init__(self, name: _Optional[str] = ..., members: _Optional[_Iterable[_Union[NetworkAPI.Group.Member, _Mapping]]] = ...) -> None: ...
    class GroupChange(_message.Message):
        __slots__ = ("invite", "join", "kick", "status")
        INVITE_FIELD_NUMBER: _ClassVar[int]
        JOIN_FIELD_NUMBER: _ClassVar[int]
        KICK_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        invite: NetworkAPI.GroupInvite
        join: NetworkAPI.GroupJoin
        kick: NetworkAPI.GroupKick
        status: NetworkAPI.GroupStatus
        def __init__(self, invite: _Optional[_Union[NetworkAPI.GroupInvite, _Mapping]] = ..., join: _Optional[_Union[NetworkAPI.GroupJoin, _Mapping]] = ..., kick: _Optional[_Union[NetworkAPI.GroupKick, _Mapping]] = ..., status: _Optional[_Union[NetworkAPI.GroupStatus, _Mapping]] = ...) -> None: ...
    class GroupResponse(_message.Message):
        __slots__ = ("success", "status")
        class Success(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Status(_message.Message):
            __slots__ = ("member_name", "group_name")
            MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
            GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            member_name: str
            group_name: str
            def __init__(self, member_name: _Optional[str] = ..., group_name: _Optional[str] = ...) -> None: ...
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        success: NetworkAPI.GroupResponse.Success
        status: NetworkAPI.GroupResponse.Status
        def __init__(self, success: _Optional[_Union[NetworkAPI.GroupResponse.Success, _Mapping]] = ..., status: _Optional[_Union[NetworkAPI.GroupResponse.Status, _Mapping]] = ...) -> None: ...
    class GroupStatus(_message.Message):
        __slots__ = ("member",)
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        member: NetworkAPI.Group.Member
        def __init__(self, member: _Optional[_Union[NetworkAPI.Group.Member, _Mapping]] = ...) -> None: ...
    class GroupInvite(_message.Message):
        __slots__ = ("group_info", "secret", "prospect")
        GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
        SECRET_FIELD_NUMBER: _ClassVar[int]
        PROSPECT_FIELD_NUMBER: _ClassVar[int]
        group_info: NetworkAPI.Group
        secret: str
        prospect: NetworkAPI.Group.Member
        def __init__(self, group_info: _Optional[_Union[NetworkAPI.Group, _Mapping]] = ..., secret: _Optional[str] = ..., prospect: _Optional[_Union[NetworkAPI.Group.Member, _Mapping]] = ...) -> None: ...
    class GroupJoin(_message.Message):
        __slots__ = ("sponsor", "prospect")
        SPONSOR_FIELD_NUMBER: _ClassVar[int]
        PROSPECT_FIELD_NUMBER: _ClassVar[int]
        sponsor: NetworkAPI.Group.Member
        prospect: NetworkAPI.Group.Member
        def __init__(self, sponsor: _Optional[_Union[NetworkAPI.Group.Member, _Mapping]] = ..., prospect: _Optional[_Union[NetworkAPI.Group.Member, _Mapping]] = ...) -> None: ...
    class GroupKick(_message.Message):
        __slots__ = ("member",)
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        member: NetworkAPI.Group.Member
        def __init__(self, member: _Optional[_Union[NetworkAPI.Group.Member, _Mapping]] = ...) -> None: ...
    class ServerState(_message.Message):
        __slots__ = ("local_ip", "public_ip", "port")
        LOCAL_IP_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        local_ip: str
        public_ip: str
        port: int
        def __init__(self, local_ip: _Optional[str] = ..., public_ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...
    class Action(_message.Message):
        __slots__ = ("clear", "trigger", "transport", "prop", "timer", "message_", "macro", "look", "stage", "status", "status_response", "two_step_trigger", "preroll_complete")
        class API_Clear(_message.Message):
            __slots__ = ("layer", "group_identifier")
            class Layer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                LAYER_UNKNOWN: _ClassVar[NetworkAPI.Action.API_Clear.Layer]
                LAYER_VIDEO_INPUT: _ClassVar[NetworkAPI.Action.API_Clear.Layer]
                LAYER_MEDIA: _ClassVar[NetworkAPI.Action.API_Clear.Layer]
                LAYER_PRESENTATION: _ClassVar[NetworkAPI.Action.API_Clear.Layer]
                LAYER_ANNOUNCEMENT: _ClassVar[NetworkAPI.Action.API_Clear.Layer]
                LAYER_PROP: _ClassVar[NetworkAPI.Action.API_Clear.Layer]
                LAYER_MESSAGE: _ClassVar[NetworkAPI.Action.API_Clear.Layer]
                LAYER_AUDIO: _ClassVar[NetworkAPI.Action.API_Clear.Layer]
            LAYER_UNKNOWN: NetworkAPI.Action.API_Clear.Layer
            LAYER_VIDEO_INPUT: NetworkAPI.Action.API_Clear.Layer
            LAYER_MEDIA: NetworkAPI.Action.API_Clear.Layer
            LAYER_PRESENTATION: NetworkAPI.Action.API_Clear.Layer
            LAYER_ANNOUNCEMENT: NetworkAPI.Action.API_Clear.Layer
            LAYER_PROP: NetworkAPI.Action.API_Clear.Layer
            LAYER_MESSAGE: NetworkAPI.Action.API_Clear.Layer
            LAYER_AUDIO: NetworkAPI.Action.API_Clear.Layer
            LAYER_FIELD_NUMBER: _ClassVar[int]
            GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI.Action.API_Clear.Layer
            group_identifier: NetworkAPI.IndexOrNameIdentifier
            def __init__(self, layer: _Optional[_Union[NetworkAPI.Action.API_Clear.Layer, str]] = ..., group_identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
        class API_TwoStepTrigger(_message.Message):
            __slots__ = ("id", "operation", "render_time", "presentation", "media", "video_input", "audio", "prop", "message")
            class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                OPERATION_PREROLL: _ClassVar[NetworkAPI.Action.API_TwoStepTrigger.Operation]
                OPERATION_ACTIVATE: _ClassVar[NetworkAPI.Action.API_TwoStepTrigger.Operation]
            OPERATION_PREROLL: NetworkAPI.Action.API_TwoStepTrigger.Operation
            OPERATION_ACTIVATE: NetworkAPI.Action.API_TwoStepTrigger.Operation
            ID_FIELD_NUMBER: _ClassVar[int]
            OPERATION_FIELD_NUMBER: _ClassVar[int]
            RENDER_TIME_FIELD_NUMBER: _ClassVar[int]
            PRESENTATION_FIELD_NUMBER: _ClassVar[int]
            MEDIA_FIELD_NUMBER: _ClassVar[int]
            VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
            AUDIO_FIELD_NUMBER: _ClassVar[int]
            PROP_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            id: int
            operation: NetworkAPI.Action.API_TwoStepTrigger.Operation
            render_time: int
            presentation: NetworkAPI.Action.API_Trigger.Presentation
            media: NetworkAPI.Action.API_Trigger.Media
            video_input: NetworkAPI.Action.API_Trigger.VideoInput
            audio: NetworkAPI.Action.API_Trigger.Audio
            prop: NetworkAPI.Action.API_Prop.TriggerProp
            message: NetworkAPI.Action.API_Message.TriggerMessage
            def __init__(self, id: _Optional[int] = ..., operation: _Optional[_Union[NetworkAPI.Action.API_TwoStepTrigger.Operation, str]] = ..., render_time: _Optional[int] = ..., presentation: _Optional[_Union[NetworkAPI.Action.API_Trigger.Presentation, _Mapping]] = ..., media: _Optional[_Union[NetworkAPI.Action.API_Trigger.Media, _Mapping]] = ..., video_input: _Optional[_Union[NetworkAPI.Action.API_Trigger.VideoInput, _Mapping]] = ..., audio: _Optional[_Union[NetworkAPI.Action.API_Trigger.Audio, _Mapping]] = ..., prop: _Optional[_Union[NetworkAPI.Action.API_Prop.TriggerProp, _Mapping]] = ..., message: _Optional[_Union[NetworkAPI.Action.API_Message.TriggerMessage, _Mapping]] = ...) -> None: ...
        class API_PrerollComplete(_message.Message):
            __slots__ = ("id", "failed")
            ID_FIELD_NUMBER: _ClassVar[int]
            FAILED_FIELD_NUMBER: _ClassVar[int]
            id: int
            failed: bool
            def __init__(self, id: _Optional[int] = ..., failed: bool = ...) -> None: ...
        class API_Trigger(_message.Message):
            __slots__ = ("presentation", "media", "video_input", "audio")
            class Presentation(_message.Message):
                __slots__ = ("cue_index", "playlist_index_path", "library_index_path")
                class PlaylistPresentation(_message.Message):
                    __slots__ = ("index_path_components",)
                    INDEX_PATH_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
                    index_path_components: _containers.RepeatedCompositeFieldContainer[NetworkAPI.IndexOrNameIdentifier]
                    def __init__(self, index_path_components: _Optional[_Iterable[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]]] = ...) -> None: ...
                class LibraryPresentation(_message.Message):
                    __slots__ = ("library_component", "presentation_component", "cue_component")
                    LIBRARY_COMPONENT_FIELD_NUMBER: _ClassVar[int]
                    PRESENTATION_COMPONENT_FIELD_NUMBER: _ClassVar[int]
                    CUE_COMPONENT_FIELD_NUMBER: _ClassVar[int]
                    library_component: NetworkAPI.IndexOrNameIdentifier
                    presentation_component: NetworkAPI.IndexOrNameIdentifier
                    cue_component: NetworkAPI.IndexOrNameIdentifier
                    def __init__(self, library_component: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ..., presentation_component: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ..., cue_component: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
                CUE_INDEX_FIELD_NUMBER: _ClassVar[int]
                PLAYLIST_INDEX_PATH_FIELD_NUMBER: _ClassVar[int]
                LIBRARY_INDEX_PATH_FIELD_NUMBER: _ClassVar[int]
                cue_index: int
                playlist_index_path: NetworkAPI.Action.API_Trigger.Presentation.PlaylistPresentation
                library_index_path: NetworkAPI.Action.API_Trigger.Presentation.LibraryPresentation
                def __init__(self, cue_index: _Optional[int] = ..., playlist_index_path: _Optional[_Union[NetworkAPI.Action.API_Trigger.Presentation.PlaylistPresentation, _Mapping]] = ..., library_index_path: _Optional[_Union[NetworkAPI.Action.API_Trigger.Presentation.LibraryPresentation, _Mapping]] = ...) -> None: ...
            class Media(_message.Message):
                __slots__ = ("index_path_components",)
                INDEX_PATH_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
                index_path_components: _containers.RepeatedCompositeFieldContainer[NetworkAPI.IndexOrNameIdentifier]
                def __init__(self, index_path_components: _Optional[_Iterable[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]]] = ...) -> None: ...
            class VideoInput(_message.Message):
                __slots__ = ("video_input_id",)
                VIDEO_INPUT_ID_FIELD_NUMBER: _ClassVar[int]
                video_input_id: NetworkAPI.IndexOrNameIdentifier
                def __init__(self, video_input_id: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
            class Audio(_message.Message):
                __slots__ = ("index_path_components",)
                INDEX_PATH_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
                index_path_components: _containers.RepeatedCompositeFieldContainer[NetworkAPI.IndexOrNameIdentifier]
                def __init__(self, index_path_components: _Optional[_Iterable[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]]] = ...) -> None: ...
            PRESENTATION_FIELD_NUMBER: _ClassVar[int]
            MEDIA_FIELD_NUMBER: _ClassVar[int]
            VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
            AUDIO_FIELD_NUMBER: _ClassVar[int]
            presentation: NetworkAPI.Action.API_Trigger.Presentation
            media: NetworkAPI.Action.API_Trigger.Media
            video_input: NetworkAPI.Action.API_Trigger.VideoInput
            audio: NetworkAPI.Action.API_Trigger.Audio
            def __init__(self, presentation: _Optional[_Union[NetworkAPI.Action.API_Trigger.Presentation, _Mapping]] = ..., media: _Optional[_Union[NetworkAPI.Action.API_Trigger.Media, _Mapping]] = ..., video_input: _Optional[_Union[NetworkAPI.Action.API_Trigger.VideoInput, _Mapping]] = ..., audio: _Optional[_Union[NetworkAPI.Action.API_Trigger.Audio, _Mapping]] = ...) -> None: ...
        class API_Transport(_message.Message):
            __slots__ = ("layer", "play", "pause", "skip_backward", "skip_forward", "go_to_end")
            class TransportLayer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TRANSPORT_LAYER_UNKNOWN: _ClassVar[NetworkAPI.Action.API_Transport.TransportLayer]
                TRANSPORT_LAYER_PRESENTATION: _ClassVar[NetworkAPI.Action.API_Transport.TransportLayer]
                TRANSPORT_LAYER_ANNOUNCEMENT: _ClassVar[NetworkAPI.Action.API_Transport.TransportLayer]
                TRANSPORT_LAYER_AUDIO: _ClassVar[NetworkAPI.Action.API_Transport.TransportLayer]
            TRANSPORT_LAYER_UNKNOWN: NetworkAPI.Action.API_Transport.TransportLayer
            TRANSPORT_LAYER_PRESENTATION: NetworkAPI.Action.API_Transport.TransportLayer
            TRANSPORT_LAYER_ANNOUNCEMENT: NetworkAPI.Action.API_Transport.TransportLayer
            TRANSPORT_LAYER_AUDIO: NetworkAPI.Action.API_Transport.TransportLayer
            class Play(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Pause(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class SkipBackward(_message.Message):
                __slots__ = ("seconds",)
                SECONDS_FIELD_NUMBER: _ClassVar[int]
                seconds: int
                def __init__(self, seconds: _Optional[int] = ...) -> None: ...
            class SkipForward(_message.Message):
                __slots__ = ("seconds",)
                SECONDS_FIELD_NUMBER: _ClassVar[int]
                seconds: int
                def __init__(self, seconds: _Optional[int] = ...) -> None: ...
            class GoToEnd(_message.Message):
                __slots__ = ("seconds_to_end",)
                SECONDS_TO_END_FIELD_NUMBER: _ClassVar[int]
                seconds_to_end: int
                def __init__(self, seconds_to_end: _Optional[int] = ...) -> None: ...
            LAYER_FIELD_NUMBER: _ClassVar[int]
            PLAY_FIELD_NUMBER: _ClassVar[int]
            PAUSE_FIELD_NUMBER: _ClassVar[int]
            SKIP_BACKWARD_FIELD_NUMBER: _ClassVar[int]
            SKIP_FORWARD_FIELD_NUMBER: _ClassVar[int]
            GO_TO_END_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI.Action.API_Transport.TransportLayer
            play: NetworkAPI.Action.API_Transport.Play
            pause: NetworkAPI.Action.API_Transport.Pause
            skip_backward: NetworkAPI.Action.API_Transport.SkipBackward
            skip_forward: NetworkAPI.Action.API_Transport.SkipForward
            go_to_end: NetworkAPI.Action.API_Transport.GoToEnd
            def __init__(self, layer: _Optional[_Union[NetworkAPI.Action.API_Transport.TransportLayer, str]] = ..., play: _Optional[_Union[NetworkAPI.Action.API_Transport.Play, _Mapping]] = ..., pause: _Optional[_Union[NetworkAPI.Action.API_Transport.Pause, _Mapping]] = ..., skip_backward: _Optional[_Union[NetworkAPI.Action.API_Transport.SkipBackward, _Mapping]] = ..., skip_forward: _Optional[_Union[NetworkAPI.Action.API_Transport.SkipForward, _Mapping]] = ..., go_to_end: _Optional[_Union[NetworkAPI.Action.API_Transport.GoToEnd, _Mapping]] = ...) -> None: ...
        class API_Prop(_message.Message):
            __slots__ = ("trigger", "clear")
            class TriggerProp(_message.Message):
                __slots__ = ("identifier",)
                IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                identifier: NetworkAPI.IndexOrNameIdentifier
                def __init__(self, identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
            class ClearProp(_message.Message):
                __slots__ = ("identifier",)
                IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                identifier: NetworkAPI.IndexOrNameIdentifier
                def __init__(self, identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
            TRIGGER_FIELD_NUMBER: _ClassVar[int]
            CLEAR_FIELD_NUMBER: _ClassVar[int]
            trigger: NetworkAPI.Action.API_Prop.TriggerProp
            clear: NetworkAPI.Action.API_Prop.ClearProp
            def __init__(self, trigger: _Optional[_Union[NetworkAPI.Action.API_Prop.TriggerProp, _Mapping]] = ..., clear: _Optional[_Union[NetworkAPI.Action.API_Prop.ClearProp, _Mapping]] = ...) -> None: ...
        class API_Timer(_message.Message):
            __slots__ = ("start", "stop", "reset", "configure")
            class StartTimer(_message.Message):
                __slots__ = ("identifier",)
                IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                identifier: NetworkAPI.IndexOrNameIdentifier
                def __init__(self, identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
            class StopTimer(_message.Message):
                __slots__ = ("identifier",)
                IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                identifier: NetworkAPI.IndexOrNameIdentifier
                def __init__(self, identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
            class ResetTimer(_message.Message):
                __slots__ = ("identifier",)
                IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                identifier: NetworkAPI.IndexOrNameIdentifier
                def __init__(self, identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
            class ConfigureTimer(_message.Message):
                __slots__ = ("identifier", "configuration")
                IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
                identifier: NetworkAPI.IndexOrNameIdentifier
                configuration: _timers_pb2.Timer.Configuration
                def __init__(self, identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ..., configuration: _Optional[_Union[_timers_pb2.Timer.Configuration, _Mapping]] = ...) -> None: ...
            START_FIELD_NUMBER: _ClassVar[int]
            STOP_FIELD_NUMBER: _ClassVar[int]
            RESET_FIELD_NUMBER: _ClassVar[int]
            CONFIGURE_FIELD_NUMBER: _ClassVar[int]
            start: NetworkAPI.Action.API_Timer.StartTimer
            stop: NetworkAPI.Action.API_Timer.StopTimer
            reset: NetworkAPI.Action.API_Timer.ResetTimer
            configure: NetworkAPI.Action.API_Timer.ConfigureTimer
            def __init__(self, start: _Optional[_Union[NetworkAPI.Action.API_Timer.StartTimer, _Mapping]] = ..., stop: _Optional[_Union[NetworkAPI.Action.API_Timer.StopTimer, _Mapping]] = ..., reset: _Optional[_Union[NetworkAPI.Action.API_Timer.ResetTimer, _Mapping]] = ..., configure: _Optional[_Union[NetworkAPI.Action.API_Timer.ConfigureTimer, _Mapping]] = ...) -> None: ...
        class API_Message(_message.Message):
            __slots__ = ("trigger", "clear")
            class TriggerMessage(_message.Message):
                __slots__ = ("identifier", "token_values")
                IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                TOKEN_VALUES_FIELD_NUMBER: _ClassVar[int]
                identifier: NetworkAPI.IndexOrNameIdentifier
                token_values: _containers.RepeatedCompositeFieldContainer[_messages_pb2.Message.TokenValue]
                def __init__(self, identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ..., token_values: _Optional[_Iterable[_Union[_messages_pb2.Message.TokenValue, _Mapping]]] = ...) -> None: ...
            class ClearMessage(_message.Message):
                __slots__ = ("identifier",)
                IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                identifier: NetworkAPI.IndexOrNameIdentifier
                def __init__(self, identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
            TRIGGER_FIELD_NUMBER: _ClassVar[int]
            CLEAR_FIELD_NUMBER: _ClassVar[int]
            trigger: NetworkAPI.Action.API_Message.TriggerMessage
            clear: NetworkAPI.Action.API_Message.ClearMessage
            def __init__(self, trigger: _Optional[_Union[NetworkAPI.Action.API_Message.TriggerMessage, _Mapping]] = ..., clear: _Optional[_Union[NetworkAPI.Action.API_Message.ClearMessage, _Mapping]] = ...) -> None: ...
        class API_Macro(_message.Message):
            __slots__ = ("identifier",)
            IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            identifier: NetworkAPI.IndexOrNameIdentifier
            def __init__(self, identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
        class API_Look(_message.Message):
            __slots__ = ("identifier",)
            IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            identifier: NetworkAPI.IndexOrNameIdentifier
            def __init__(self, identifier: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
        class API_Stage(_message.Message):
            __slots__ = ("layouts", "message")
            class StageLayouts(_message.Message):
                __slots__ = ("layouts",)
                LAYOUTS_FIELD_NUMBER: _ClassVar[int]
                layouts: _containers.RepeatedCompositeFieldContainer[NetworkAPI.IndexOrNameIdentifierPair]
                def __init__(self, layouts: _Optional[_Iterable[_Union[NetworkAPI.IndexOrNameIdentifierPair, _Mapping]]] = ...) -> None: ...
            class StageMessage(_message.Message):
                __slots__ = ("show_message", "clear_message", "hide_message")
                class ShowMessage(_message.Message):
                    __slots__ = ("message",)
                    MESSAGE_FIELD_NUMBER: _ClassVar[int]
                    message: str
                    def __init__(self, message: _Optional[str] = ...) -> None: ...
                class ClearMessage(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class HideMessage(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                SHOW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
                CLEAR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
                HIDE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
                show_message: NetworkAPI.Action.API_Stage.StageMessage.ShowMessage
                clear_message: NetworkAPI.Action.API_Stage.StageMessage.ClearMessage
                hide_message: NetworkAPI.Action.API_Stage.StageMessage.HideMessage
                def __init__(self, show_message: _Optional[_Union[NetworkAPI.Action.API_Stage.StageMessage.ShowMessage, _Mapping]] = ..., clear_message: _Optional[_Union[NetworkAPI.Action.API_Stage.StageMessage.ClearMessage, _Mapping]] = ..., hide_message: _Optional[_Union[NetworkAPI.Action.API_Stage.StageMessage.HideMessage, _Mapping]] = ...) -> None: ...
            LAYOUTS_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            layouts: NetworkAPI.Action.API_Stage.StageLayouts
            message: NetworkAPI.Action.API_Stage.StageMessage
            def __init__(self, layouts: _Optional[_Union[NetworkAPI.Action.API_Stage.StageLayouts, _Mapping]] = ..., message: _Optional[_Union[NetworkAPI.Action.API_Stage.StageMessage, _Mapping]] = ...) -> None: ...
        class StatusRequest(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class API_Status(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class API_StatusResponse(_message.Message):
            __slots__ = ("group_definition", "status")
            GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            STATUS_FIELD_NUMBER: _ClassVar[int]
            group_definition: ProLink.GroupDefinition
            status: ProLink.MemberStatus
            def __init__(self, group_definition: _Optional[_Union[ProLink.GroupDefinition, _Mapping]] = ..., status: _Optional[_Union[ProLink.MemberStatus, _Mapping]] = ...) -> None: ...
        CLEAR_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        TRANSPORT_FIELD_NUMBER: _ClassVar[int]
        PROP_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        MESSAGE__FIELD_NUMBER: _ClassVar[int]
        MACRO_FIELD_NUMBER: _ClassVar[int]
        LOOK_FIELD_NUMBER: _ClassVar[int]
        STAGE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        TWO_STEP_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PREROLL_COMPLETE_FIELD_NUMBER: _ClassVar[int]
        clear: NetworkAPI.Action.API_Clear
        trigger: NetworkAPI.Action.API_Trigger
        transport: NetworkAPI.Action.API_Transport
        prop: NetworkAPI.Action.API_Prop
        timer: NetworkAPI.Action.API_Timer
        message_: NetworkAPI.Action.API_Message
        macro: NetworkAPI.Action.API_Macro
        look: NetworkAPI.Action.API_Look
        stage: NetworkAPI.Action.API_Stage
        status: NetworkAPI.Action.API_Status
        status_response: NetworkAPI.Action.API_StatusResponse
        two_step_trigger: NetworkAPI.Action.API_TwoStepTrigger
        preroll_complete: NetworkAPI.Action.API_PrerollComplete
        def __init__(self, clear: _Optional[_Union[NetworkAPI.Action.API_Clear, _Mapping]] = ..., trigger: _Optional[_Union[NetworkAPI.Action.API_Trigger, _Mapping]] = ..., transport: _Optional[_Union[NetworkAPI.Action.API_Transport, _Mapping]] = ..., prop: _Optional[_Union[NetworkAPI.Action.API_Prop, _Mapping]] = ..., timer: _Optional[_Union[NetworkAPI.Action.API_Timer, _Mapping]] = ..., message_: _Optional[_Union[NetworkAPI.Action.API_Message, _Mapping]] = ..., macro: _Optional[_Union[NetworkAPI.Action.API_Macro, _Mapping]] = ..., look: _Optional[_Union[NetworkAPI.Action.API_Look, _Mapping]] = ..., stage: _Optional[_Union[NetworkAPI.Action.API_Stage, _Mapping]] = ..., status: _Optional[_Union[NetworkAPI.Action.API_Status, _Mapping]] = ..., status_response: _Optional[_Union[NetworkAPI.Action.API_StatusResponse, _Mapping]] = ..., two_step_trigger: _Optional[_Union[NetworkAPI.Action.API_TwoStepTrigger, _Mapping]] = ..., preroll_complete: _Optional[_Union[NetworkAPI.Action.API_PrerollComplete, _Mapping]] = ...) -> None: ...
    class IndexOrNameIdentifier(_message.Message):
        __slots__ = ("index", "name")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        index: int
        name: str
        def __init__(self, index: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    class IndexOrNameIdentifierPair(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: NetworkAPI.IndexOrNameIdentifier
        value: NetworkAPI.IndexOrNameIdentifier
        def __init__(self, key: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ..., value: _Optional[_Union[NetworkAPI.IndexOrNameIdentifier, _Mapping]] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SERVER_STATE_FIELD_NUMBER: _ClassVar[int]
    GROUP_CHANGE_FIELD_NUMBER: _ClassVar[int]
    GROUP_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    action: NetworkAPI.Action
    server_state: NetworkAPI.ServerState
    group_change: NetworkAPI.GroupChange
    group_response: NetworkAPI.GroupResponse
    def __init__(self, action: _Optional[_Union[NetworkAPI.Action, _Mapping]] = ..., server_state: _Optional[_Union[NetworkAPI.ServerState, _Mapping]] = ..., group_change: _Optional[_Union[NetworkAPI.GroupChange, _Mapping]] = ..., group_response: _Optional[_Union[NetworkAPI.GroupResponse, _Mapping]] = ...) -> None: ...
