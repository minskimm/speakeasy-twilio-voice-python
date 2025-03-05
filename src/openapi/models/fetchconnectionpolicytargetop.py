"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .voice_v1_connection_policy_connection_policy_target import (
    VoiceV1ConnectionPolicyConnectionPolicyTarget,
    VoiceV1ConnectionPolicyConnectionPolicyTargetTypedDict,
)
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict

FETCH_CONNECTION_POLICY_TARGET_OP_SERVERS = [
    "https://voice.twilio.com",
]


class FetchConnectionPolicyTargetRequestTypedDict(TypedDict):
    connection_policy_sid: str
    r"""The SID of the Connection Policy that owns the Target."""
    sid: str
    r"""The unique string that we created to identify the Target resource to fetch."""


class FetchConnectionPolicyTargetRequest(BaseModel):
    connection_policy_sid: Annotated[
        str,
        pydantic.Field(alias="ConnectionPolicySid"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The SID of the Connection Policy that owns the Target."""

    sid: Annotated[
        str,
        pydantic.Field(alias="Sid"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The unique string that we created to identify the Target resource to fetch."""


class FetchConnectionPolicyTargetResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: VoiceV1ConnectionPolicyConnectionPolicyTargetTypedDict


class FetchConnectionPolicyTargetResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: VoiceV1ConnectionPolicyConnectionPolicyTarget
