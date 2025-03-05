# VoiceV1ByocTrunkSDK
(*voice_v1_byoc_trunk*)

## Overview

### Available Operations

* [create_byoc_trunk](#create_byoc_trunk)
* [list_byoc_trunk](#list_byoc_trunk)
* [fetch_byoc_trunk](#fetch_byoc_trunk)
* [update_byoc_trunk](#update_byoc_trunk)
* [delete_byoc_trunk](#delete_byoc_trunk)

## create_byoc_trunk

### Example Usage

```python
import openapi
from openapi import SDK

with SDK(
    security=openapi.Security(
        username="",
        password="",
    ),
) as sdk:

    res = sdk.voice_v1_byoc_trunk.create_byoc_trunk(request={
        "friendly_name": "friendly_name",
        "voice_url": "https://byoc.example.com/twilio/app",
        "voice_method": openapi.CreateByocTrunkVoiceMethod.POST,
        "voice_fallback_url": "https://byoc.example.com/twilio/fallback",
        "voice_fallback_method": openapi.CreateByocTrunkVoiceFallbackMethod.POST,
        "status_callback_url": "https://byoc.example.com/twilio/status_callback",
        "status_callback_method": openapi.CreateByocTrunkStatusCallbackMethod.POST,
        "cnam_lookup_enabled": False,
        "connection_policy_sid": "NYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "from_domain_sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.CreateByocTrunkCreateByocTrunkRequest](../../models/createbyoctrunkcreatebyoctrunkrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |
| `server_url`                                                                                          | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | An optional server URL to use.                                                                        |

### Response

**[models.CreateByocTrunkResponse](../../models/createbyoctrunkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_byoc_trunk

### Example Usage

```python
import openapi
from openapi import SDK

with SDK(
    security=openapi.Security(
        username="",
        password="",
    ),
) as sdk:

    res = sdk.voice_v1_byoc_trunk.list_byoc_trunk()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `page_size`                                                                                 | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | How many resources to return in each list page. The default is 50, and the maximum is 1000. |
| `page`                                                                                      | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | The page index. This value is simply for client state.                                      |
| `page_token`                                                                                | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The page token. This is provided by the API.                                                |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |
| `server_url`                                                                                | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | An optional server URL to use.                                                              |

### Response

**[models.ListByocTrunkResponse](../../models/listbyoctrunkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## fetch_byoc_trunk

### Example Usage

```python
import openapi
from openapi import SDK

with SDK(
    security=openapi.Security(
        username="",
        password="",
    ),
) as sdk:

    res = sdk.voice_v1_byoc_trunk.fetch_byoc_trunk(sid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `sid`                                                                                 | *str*                                                                                 | :heavy_check_mark:                                                                    | The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch. |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |
| `server_url`                                                                          | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | An optional server URL to use.                                                        |

### Response

**[models.FetchByocTrunkResponse](../../models/fetchbyoctrunkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_byoc_trunk

### Example Usage

```python
import openapi
from openapi import SDK

with SDK(
    security=openapi.Security(
        username="",
        password="",
    ),
) as sdk:

    res = sdk.voice_v1_byoc_trunk.update_byoc_trunk(sid="<id>", friendly_name="update_name", voice_url="https://byoc.example.com/twilio_updated/app", voice_method=openapi.UpdateByocTrunkVoiceMethod.GET, voice_fallback_url="https://byoc.example.com/twilio_updated/fallback", voice_fallback_method=openapi.UpdateByocTrunkVoiceFallbackMethod.GET, status_callback_url="https://byoc.example.com/twilio_updated/status_callback", status_callback_method=openapi.UpdateByocTrunkStatusCallbackMethod.GET, cnam_lookup_enabled=True, connection_policy_sid="NYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", from_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sid`                                                                                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update.                                                                                                                                                                                                                                                                                                 |
| `friendly_name`                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.                                                                                                                                                                                                                                                                  |
| `voice_url`                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The URL we should call when the BYOC Trunk receives a call.                                                                                                                                                                                                                                                                                                                            |
| `voice_method`                                                                                                                                                                                                                                                                                                                                                                         | [Optional[models.UpdateByocTrunkVoiceMethod]](../../models/updatebyoctrunkvoicemethod.md)                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The HTTP method we should use to call `voice_url`                                                                                                                                                                                                                                                                                                                                      |
| `voice_fallback_url`                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.                                                                                                                                                                                                                                                                     |
| `voice_fallback_method`                                                                                                                                                                                                                                                                                                                                                                | [Optional[models.UpdateByocTrunkVoiceFallbackMethod]](../../models/updatebyoctrunkvoicefallbackmethod.md)                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.                                                                                                                                                                                                                                                                                                   |
| `status_callback_url`                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The URL that we should call to pass status parameters (such as call ended) to your application.                                                                                                                                                                                                                                                                                        |
| `status_callback_method`                                                                                                                                                                                                                                                                                                                                                               | [Optional[models.UpdateByocTrunkStatusCallbackMethod]](../../models/updatebyoctrunkstatuscallbackmethod.md)                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.                                                                                                                                                                                                                                                                                                  |
| `cnam_lookup_enabled`                                                                                                                                                                                                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.                                                                 |
| `connection_policy_sid`                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.                                                                                                                                                                                                                                                                      |
| `from_domain_sid`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to "call back" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to "sip.twilio.com". |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |
| `server_url`                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | An optional server URL to use.                                                                                                                                                                                                                                                                                                                                                         |

### Response

**[models.UpdateByocTrunkResponse](../../models/updatebyoctrunkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_byoc_trunk

### Example Usage

```python
import openapi
from openapi import SDK

with SDK(
    security=openapi.Security(
        username="",
        password="",
    ),
) as sdk:

    sdk.voice_v1_byoc_trunk.delete_byoc_trunk(sid="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `sid`                                                                                  | *str*                                                                                  | :heavy_check_mark:                                                                     | The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete. |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |
| `server_url`                                                                           | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | An optional server URL to use.                                                         |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |