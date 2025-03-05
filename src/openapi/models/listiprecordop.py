"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .voice_v1_ip_record import VoiceV1IPRecord, VoiceV1IPRecordTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from openapi.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict

LIST_IP_RECORD_OP_SERVERS = [
    "https://voice.twilio.com",
]


class ListIPRecordRequestTypedDict(TypedDict):
    page_size: NotRequired[int]
    r"""How many resources to return in each list page. The default is 50, and the maximum is 1000."""
    page: NotRequired[int]
    r"""The page index. This value is simply for client state."""
    page_token: NotRequired[str]
    r"""The page token. This is provided by the API."""


class ListIPRecordRequest(BaseModel):
    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="PageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""How many resources to return in each list page. The default is 50, and the maximum is 1000."""

    page: Annotated[
        Optional[int],
        pydantic.Field(alias="Page"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The page index. This value is simply for client state."""

    page_token: Annotated[
        Optional[str],
        pydantic.Field(alias="PageToken"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The page token. This is provided by the API."""


class ListIPRecordMetaTypedDict(TypedDict):
    first_page_url: NotRequired[str]
    key: NotRequired[str]
    next_page_url: NotRequired[Nullable[str]]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_url: NotRequired[Nullable[str]]
    url: NotRequired[str]


class ListIPRecordMeta(BaseModel):
    first_page_url: Optional[str] = None

    key: Optional[str] = None

    next_page_url: OptionalNullable[str] = UNSET

    page: Optional[int] = None

    page_size: Optional[int] = None

    previous_page_url: OptionalNullable[str] = UNSET

    url: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "first_page_url",
            "key",
            "next_page_url",
            "page",
            "page_size",
            "previous_page_url",
            "url",
        ]
        nullable_fields = ["next_page_url", "previous_page_url"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class ListIPRecordListIPRecordResponseTypedDict(TypedDict):
    r"""OK"""

    ip_records: NotRequired[List[VoiceV1IPRecordTypedDict]]
    meta: NotRequired[ListIPRecordMetaTypedDict]


class ListIPRecordListIPRecordResponse(BaseModel):
    r"""OK"""

    ip_records: Optional[List[VoiceV1IPRecord]] = None

    meta: Optional[ListIPRecordMeta] = None


class ListIPRecordResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ListIPRecordListIPRecordResponseTypedDict


class ListIPRecordResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ListIPRecordListIPRecordResponse
