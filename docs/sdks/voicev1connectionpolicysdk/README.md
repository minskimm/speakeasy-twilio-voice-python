# VoiceV1ConnectionPolicySDK
(*voice_v1_connection_policy*)

## Overview

### Available Operations

* [create_connection_policy](#create_connection_policy)
* [list_connection_policy](#list_connection_policy)
* [fetch_connection_policy](#fetch_connection_policy)
* [update_connection_policy](#update_connection_policy)
* [delete_connection_policy](#delete_connection_policy)

## create_connection_policy

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

    res = sdk.voice_v1_connection_policy.create_connection_policy(request={
        "friendly_name": "friendly_name",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                         | [models.CreateConnectionPolicyCreateConnectionPolicyRequest](../../models/createconnectionpolicycreateconnectionpolicyrequest.md) | :heavy_check_mark:                                                                                                                | The request object to use for the request.                                                                                        |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |
| `server_url`                                                                                                                      | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | An optional server URL to use.                                                                                                    |

### Response

**[models.CreateConnectionPolicyResponse](../../models/createconnectionpolicyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_connection_policy

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

    res = sdk.voice_v1_connection_policy.list_connection_policy()

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

**[models.ListConnectionPolicyResponse](../../models/listconnectionpolicyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## fetch_connection_policy

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

    res = sdk.voice_v1_connection_policy.fetch_connection_policy(sid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `sid`                                                                                  | *str*                                                                                  | :heavy_check_mark:                                                                     | The unique string that we created to identify the Connection Policy resource to fetch. |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |
| `server_url`                                                                           | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | An optional server URL to use.                                                         |

### Response

**[models.FetchConnectionPolicyResponse](../../models/fetchconnectionpolicyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_connection_policy

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

    res = sdk.voice_v1_connection_policy.update_connection_policy(sid="<id>", friendly_name="updated_name")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `sid`                                                                                                                 | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | The unique string that we created to identify the Connection Policy resource to update.                               |
| `friendly_name`                                                                                                       | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |
| `server_url`                                                                                                          | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | An optional server URL to use.                                                                                        |

### Response

**[models.UpdateConnectionPolicyResponse](../../models/updateconnectionpolicyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_connection_policy

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

    sdk.voice_v1_connection_policy.delete_connection_policy(sid="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `sid`                                                                                   | *str*                                                                                   | :heavy_check_mark:                                                                      | The unique string that we created to identify the Connection Policy resource to delete. |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |
| `server_url`                                                                            | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | An optional server URL to use.                                                          |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |