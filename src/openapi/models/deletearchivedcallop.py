"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import date
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict

DELETE_ARCHIVED_CALL_OP_SERVERS = [
    "https://voice.twilio.com",
]


class DeleteArchivedCallRequestTypedDict(TypedDict):
    date_: date
    r"""The date of the Call in UTC."""
    sid: str
    r"""The Twilio-provided Call SID that uniquely identifies the Call resource to delete"""


class DeleteArchivedCallRequest(BaseModel):
    date_: Annotated[
        date,
        pydantic.Field(alias="Date"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The date of the Call in UTC."""

    sid: Annotated[
        str,
        pydantic.Field(alias="Sid"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The Twilio-provided Call SID that uniquely identifies the Call resource to delete"""
