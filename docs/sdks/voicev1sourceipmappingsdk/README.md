# VoiceV1SourceIPMappingSDK
(*voice_v1_source_ip_mapping*)

## Overview

### Available Operations

* [create_source_ip_mapping](#create_source_ip_mapping)
* [list_source_ip_mapping](#list_source_ip_mapping)
* [fetch_source_ip_mapping](#fetch_source_ip_mapping)
* [update_source_ip_mapping](#update_source_ip_mapping)
* [delete_source_ip_mapping](#delete_source_ip_mapping)

## create_source_ip_mapping

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

    res = sdk.voice_v1_source_ip_mapping.create_source_ip_mapping(request={
        "ip_record_sid": "ILaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "sip_domain_sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                     | [models.CreateSourceIPMappingCreateSourceIPMappingRequest](../../models/createsourceipmappingcreatesourceipmappingrequest.md) | :heavy_check_mark:                                                                                                            | The request object to use for the request.                                                                                    |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |
| `server_url`                                                                                                                  | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | An optional server URL to use.                                                                                                |

### Response

**[models.CreateSourceIPMappingResponse](../../models/createsourceipmappingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_source_ip_mapping

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

    res = sdk.voice_v1_source_ip_mapping.list_source_ip_mapping()

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

**[models.ListSourceIPMappingResponse](../../models/listsourceipmappingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## fetch_source_ip_mapping

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

    res = sdk.voice_v1_source_ip_mapping.fetch_source_ip_mapping(sid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `sid`                                                                                | *str*                                                                                | :heavy_check_mark:                                                                   | The Twilio-provided string that uniquely identifies the IP Record resource to fetch. |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |
| `server_url`                                                                         | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | An optional server URL to use.                                                       |

### Response

**[models.FetchSourceIPMappingResponse](../../models/fetchsourceipmappingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_source_ip_mapping

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

    res = sdk.voice_v1_source_ip_mapping.update_source_ip_mapping(sid="<id>", sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `sid`                                                                                 | *str*                                                                                 | :heavy_check_mark:                                                                    | The Twilio-provided string that uniquely identifies the IP Record resource to update. |
| `sip_domain_sid`                                                                      | *str*                                                                                 | :heavy_check_mark:                                                                    | The SID of the SIP Domain that the IP Record should be mapped to.                     |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |
| `server_url`                                                                          | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | An optional server URL to use.                                                        |

### Response

**[models.UpdateSourceIPMappingResponse](../../models/updatesourceipmappingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_source_ip_mapping

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

    sdk.voice_v1_source_ip_mapping.delete_source_ip_mapping(sid="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `sid`                                                                                 | *str*                                                                                 | :heavy_check_mark:                                                                    | The Twilio-provided string that uniquely identifies the IP Record resource to delete. |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |
| `server_url`                                                                          | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | An optional server URL to use.                                                        |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |