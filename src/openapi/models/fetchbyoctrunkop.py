"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .voice_v1_byoc_trunk import VoiceV1ByocTrunk, VoiceV1ByocTrunkTypedDict
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict

FETCH_BYOC_TRUNK_OP_SERVERS = [
    "https://voice.twilio.com",
]


class FetchByocTrunkRequestTypedDict(TypedDict):
    sid: str
    r"""The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch."""


class FetchByocTrunkRequest(BaseModel):
    sid: Annotated[
        str,
        pydantic.Field(alias="Sid"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch."""


class FetchByocTrunkResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: VoiceV1ByocTrunkTypedDict


class FetchByocTrunkResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: VoiceV1ByocTrunk
