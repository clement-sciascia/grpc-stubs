"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from builtins import (
    int,
    type,
)

from google.protobuf.descriptor import (
    Descriptor,
    EnumDescriptor,
    FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper,
)

from google.protobuf.message import (
    Message,
)

from typing import (
    NewType,
    Text,
)

from typing_extensions import (
    Literal,
    TypeAlias,
)


DESCRIPTOR: FileDescriptor

class HealthCheckRequest(Message):
    DESCRIPTOR: Descriptor
    SERVICE_FIELD_NUMBER: int
    service: Text
    def __init__(self,
        *,
        service: Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: Literal["service",b"service"]) -> None: ...

class HealthCheckResponse(Message):
    DESCRIPTOR: Descriptor
    class _ServingStatus:
        ValueType = NewType('ValueType', int)
        V: TypeAlias = ValueType
    class _ServingStatusEnumTypeWrapper(_EnumTypeWrapper[HealthCheckResponse._ServingStatus.ValueType], type):
        DESCRIPTOR: EnumDescriptor
        UNKNOWN: HealthCheckResponse._ServingStatus.ValueType  # 0
        SERVING: HealthCheckResponse._ServingStatus.ValueType  # 1
        NOT_SERVING: HealthCheckResponse._ServingStatus.ValueType  # 2
        SERVICE_UNKNOWN: HealthCheckResponse._ServingStatus.ValueType  # 3
        """Used only by the Watch method."""

    class ServingStatus(_ServingStatus, metaclass=_ServingStatusEnumTypeWrapper):
        pass

    UNKNOWN: HealthCheckResponse.ServingStatus.ValueType  # 0
    SERVING: HealthCheckResponse.ServingStatus.ValueType  # 1
    NOT_SERVING: HealthCheckResponse.ServingStatus.ValueType  # 2
    SERVICE_UNKNOWN: HealthCheckResponse.ServingStatus.ValueType  # 3
    """Used only by the Watch method."""


    STATUS_FIELD_NUMBER: int
    status: HealthCheckResponse.ServingStatus.ValueType
    def __init__(self,
        *,
        status: HealthCheckResponse.ServingStatus.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: Literal["status",b"status"]) -> None: ...