"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class VoiceMethod(str, Enum):
    r"""The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`."""

    GET = "GET"
    POST = "POST"


class VoiceFallbackMethod(str, Enum):
    r"""The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`."""

    GET = "GET"
    POST = "POST"


class StatusCallbackMethod(str, Enum):
    r"""The HTTP method we use to call `status_callback_url`. Either `GET` or `POST`."""

    GET = "GET"
    POST = "POST"


class VoiceV1ByocTrunkTypedDict(TypedDict):
    account_sid: NotRequired[Nullable[str]]
    r"""The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the BYOC Trunk resource."""
    sid: NotRequired[Nullable[str]]
    r"""The unique string that that we created to identify the BYOC Trunk resource."""
    friendly_name: NotRequired[Nullable[str]]
    r"""The string that you assigned to describe the resource."""
    voice_url: NotRequired[Nullable[str]]
    r"""The URL we call using the `voice_method` when the BYOC Trunk receives a call."""
    voice_method: NotRequired[Nullable[VoiceMethod]]
    r"""The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`."""
    voice_fallback_url: NotRequired[Nullable[str]]
    r"""The URL that we call when an error occurs while retrieving or executing the TwiML requested from `voice_url`."""
    voice_fallback_method: NotRequired[Nullable[VoiceFallbackMethod]]
    r"""The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`."""
    status_callback_url: NotRequired[Nullable[str]]
    r"""The URL that we call to pass status parameters (such as call ended) to your application."""
    status_callback_method: NotRequired[Nullable[StatusCallbackMethod]]
    r"""The HTTP method we use to call `status_callback_url`. Either `GET` or `POST`."""
    cnam_lookup_enabled: NotRequired[Nullable[bool]]
    r"""Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information."""
    connection_policy_sid: NotRequired[Nullable[str]]
    r"""The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure."""
    from_domain_sid: NotRequired[Nullable[str]]
    r"""The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \"call back\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \"sip.twilio.com\"."""
    date_created: NotRequired[Nullable[datetime]]
    r"""The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format."""
    date_updated: NotRequired[Nullable[datetime]]
    r"""The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format."""
    url: NotRequired[Nullable[str]]
    r"""The absolute URL of the resource."""


class VoiceV1ByocTrunk(BaseModel):
    account_sid: OptionalNullable[str] = UNSET
    r"""The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the BYOC Trunk resource."""

    sid: OptionalNullable[str] = UNSET
    r"""The unique string that that we created to identify the BYOC Trunk resource."""

    friendly_name: OptionalNullable[str] = UNSET
    r"""The string that you assigned to describe the resource."""

    voice_url: OptionalNullable[str] = UNSET
    r"""The URL we call using the `voice_method` when the BYOC Trunk receives a call."""

    voice_method: OptionalNullable[VoiceMethod] = UNSET
    r"""The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`."""

    voice_fallback_url: OptionalNullable[str] = UNSET
    r"""The URL that we call when an error occurs while retrieving or executing the TwiML requested from `voice_url`."""

    voice_fallback_method: OptionalNullable[VoiceFallbackMethod] = UNSET
    r"""The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`."""

    status_callback_url: OptionalNullable[str] = UNSET
    r"""The URL that we call to pass status parameters (such as call ended) to your application."""

    status_callback_method: OptionalNullable[StatusCallbackMethod] = UNSET
    r"""The HTTP method we use to call `status_callback_url`. Either `GET` or `POST`."""

    cnam_lookup_enabled: OptionalNullable[bool] = UNSET
    r"""Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information."""

    connection_policy_sid: OptionalNullable[str] = UNSET
    r"""The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure."""

    from_domain_sid: OptionalNullable[str] = UNSET
    r"""The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \"call back\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \"sip.twilio.com\"."""

    date_created: OptionalNullable[datetime] = UNSET
    r"""The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format."""

    date_updated: OptionalNullable[datetime] = UNSET
    r"""The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format."""

    url: OptionalNullable[str] = UNSET
    r"""The absolute URL of the resource."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "account_sid",
            "sid",
            "friendly_name",
            "voice_url",
            "voice_method",
            "voice_fallback_url",
            "voice_fallback_method",
            "status_callback_url",
            "status_callback_method",
            "cnam_lookup_enabled",
            "connection_policy_sid",
            "from_domain_sid",
            "date_created",
            "date_updated",
            "url",
        ]
        nullable_fields = [
            "account_sid",
            "sid",
            "friendly_name",
            "voice_url",
            "voice_method",
            "voice_fallback_url",
            "voice_fallback_method",
            "status_callback_url",
            "status_callback_method",
            "cnam_lookup_enabled",
            "connection_policy_sid",
            "from_domain_sid",
            "date_created",
            "date_updated",
            "url",
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
