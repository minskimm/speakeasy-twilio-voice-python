"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict

DELETE_CONNECTION_POLICY_OP_SERVERS = [
    "https://voice.twilio.com",
]


class DeleteConnectionPolicyRequestTypedDict(TypedDict):
    sid: str
    r"""The unique string that we created to identify the Connection Policy resource to delete."""


class DeleteConnectionPolicyRequest(BaseModel):
    sid: Annotated[
        str,
        pydantic.Field(alias="Sid"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The unique string that we created to identify the Connection Policy resource to delete."""
