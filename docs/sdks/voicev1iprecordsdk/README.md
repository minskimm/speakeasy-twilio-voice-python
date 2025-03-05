# VoiceV1IPRecordSDK
(*voice_v1_ip_record*)

## Overview

### Available Operations

* [create_ip_record](#create_ip_record)
* [list_ip_record](#list_ip_record)
* [fetch_ip_record](#fetch_ip_record)
* [update_ip_record](#update_ip_record)
* [delete_ip_record](#delete_ip_record)

## create_ip_record

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

    res = sdk.voice_v1_ip_record.create_ip_record(request={
        "ip_address": "10.2.3.4",
        "friendly_name": "friendly_name",
        "cidr_prefix_length": 30,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`                                                                                         | [models.CreateIPRecordCreateIPRecordRequest](../../models/createiprecordcreateiprecordrequest.md) | :heavy_check_mark:                                                                                | The request object to use for the request.                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |
| `server_url`                                                                                      | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | An optional server URL to use.                                                                    |

### Response

**[models.CreateIPRecordResponse](../../models/createiprecordresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_ip_record

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

    res = sdk.voice_v1_ip_record.list_ip_record()

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

**[models.ListIPRecordResponse](../../models/listiprecordresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## fetch_ip_record

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

    res = sdk.voice_v1_ip_record.fetch_ip_record(sid="<id>")

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

**[models.FetchIPRecordResponse](../../models/fetchiprecordresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_ip_record

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

    res = sdk.voice_v1_ip_record.update_ip_record(sid="<id>", friendly_name="update_name")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `sid`                                                                                                                 | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | The Twilio-provided string that uniquely identifies the IP Record resource to update.                                 |
| `friendly_name`                                                                                                       | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |
| `server_url`                                                                                                          | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | An optional server URL to use.                                                                                        |

### Response

**[models.UpdateIPRecordResponse](../../models/updateiprecordresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_ip_record

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

    sdk.voice_v1_ip_record.delete_ip_record(sid="<id>")

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