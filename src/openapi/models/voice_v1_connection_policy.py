"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class LinksTypedDict(TypedDict):
    r"""The URLs of related resources."""


class Links(BaseModel):
    r"""The URLs of related resources."""


class VoiceV1ConnectionPolicyTypedDict(TypedDict):
    account_sid: NotRequired[Nullable[str]]
    r"""The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Connection Policy resource."""
    sid: NotRequired[Nullable[str]]
    r"""The unique string that we created to identify the Connection Policy resource."""
    friendly_name: NotRequired[Nullable[str]]
    r"""The string that you assigned to describe the resource."""
    date_created: NotRequired[Nullable[datetime]]
    r"""The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format."""
    date_updated: NotRequired[Nullable[datetime]]
    r"""The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format."""
    url: NotRequired[Nullable[str]]
    r"""The absolute URL of the resource."""
    links: NotRequired[Nullable[LinksTypedDict]]
    r"""The URLs of related resources."""


class VoiceV1ConnectionPolicy(BaseModel):
    account_sid: OptionalNullable[str] = UNSET
    r"""The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Connection Policy resource."""

    sid: OptionalNullable[str] = UNSET
    r"""The unique string that we created to identify the Connection Policy resource."""

    friendly_name: OptionalNullable[str] = UNSET
    r"""The string that you assigned to describe the resource."""

    date_created: OptionalNullable[datetime] = UNSET
    r"""The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format."""

    date_updated: OptionalNullable[datetime] = UNSET
    r"""The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format."""

    url: OptionalNullable[str] = UNSET
    r"""The absolute URL of the resource."""

    links: OptionalNullable[Links] = UNSET
    r"""The URLs of related resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "account_sid",
            "sid",
            "friendly_name",
            "date_created",
            "date_updated",
            "url",
            "links",
        ]
        nullable_fields = [
            "account_sid",
            "sid",
            "friendly_name",
            "date_created",
            "date_updated",
            "url",
            "links",
        ]
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
