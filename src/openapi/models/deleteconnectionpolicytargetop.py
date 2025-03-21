"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict

DELETE_CONNECTION_POLICY_TARGET_OP_SERVERS = [
    "https://voice.twilio.com",
]


class DeleteConnectionPolicyTargetRequestTypedDict(TypedDict):
    connection_policy_sid: str
    r"""The SID of the Connection Policy that owns the Target."""
    sid: str
    r"""The unique string that we created to identify the Target resource to delete."""


class DeleteConnectionPolicyTargetRequest(BaseModel):
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
    r"""The unique string that we created to identify the Target resource to delete."""
