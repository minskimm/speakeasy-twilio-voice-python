# VoiceV1ConnectionPolicyTarget
(*voice_v1_connection_policy_target*)

## Overview

### Available Operations

* [create_connection_policy_target](#create_connection_policy_target)
* [list_connection_policy_target](#list_connection_policy_target)
* [fetch_connection_policy_target](#fetch_connection_policy_target)
* [update_connection_policy_target](#update_connection_policy_target)
* [delete_connection_policy_target](#delete_connection_policy_target)

## create_connection_policy_target

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

    res = sdk.voice_v1_connection_policy_target.create_connection_policy_target(connection_policy_sid="<id>", target="sip:sip-box.com:1234", friendly_name="friendly_name", priority=1, weight=20, enabled=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connection_policy_sid`                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                        | The SID of the Connection Policy that owns the Target.                                                                                                                                                                                                                                                    |
| `target`                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                        | The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.                                                                                                                                                                                            |
| `friendly_name`                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                        | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.                                                                                                                                                                                     |
| `priority`                                                                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                        | The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.                                                                                                                                       |
| `weight`                                                                                                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                        | The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority. |
| `enabled`                                                                                                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                        | Whether the Target is enabled. The default is `true`.                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                       |
| `server_url`                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                        | An optional server URL to use.                                                                                                                                                                                                                                                                            |

### Response

**[models.CreateConnectionPolicyTargetResponse](../../models/createconnectionpolicytargetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_connection_policy_target

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

    res = sdk.voice_v1_connection_policy_target.list_connection_policy_target(connection_policy_sid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `connection_policy_sid`                                                                     | *str*                                                                                       | :heavy_check_mark:                                                                          | The SID of the Connection Policy from which to read the Targets.                            |
| `page_size`                                                                                 | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | How many resources to return in each list page. The default is 50, and the maximum is 1000. |
| `page`                                                                                      | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | The page index. This value is simply for client state.                                      |
| `page_token`                                                                                | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The page token. This is provided by the API.                                                |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |
| `server_url`                                                                                | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | An optional server URL to use.                                                              |

### Response

**[models.ListConnectionPolicyTargetResponse](../../models/listconnectionpolicytargetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## fetch_connection_policy_target

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

    res = sdk.voice_v1_connection_policy_target.fetch_connection_policy_target(connection_policy_sid="<id>", sid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `connection_policy_sid`                                                     | *str*                                                                       | :heavy_check_mark:                                                          | The SID of the Connection Policy that owns the Target.                      |
| `sid`                                                                       | *str*                                                                       | :heavy_check_mark:                                                          | The unique string that we created to identify the Target resource to fetch. |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |
| `server_url`                                                                | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | An optional server URL to use.                                              |

### Response

**[models.FetchConnectionPolicyTargetResponse](../../models/fetchconnectionpolicytargetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_connection_policy_target

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

    res = sdk.voice_v1_connection_policy_target.update_connection_policy_target(connection_policy_sid="<id>", sid="<id>", friendly_name="updated_name", target="sip:sip-updated.com:4321", priority=2, weight=10, enabled=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connection_policy_sid`                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                 | The SID of the Connection Policy that owns the Target.                                                                                                                                                                                                                             |
| `sid`                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                 | The unique string that we created to identify the Target resource to update.                                                                                                                                                                                                       |
| `friendly_name`                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.                                                                                                                                                              |
| `target`                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.                                                                                                                                                                     |
| `priority`                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.                                                                                                                                       |
| `weight`                                                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority. |
| `enabled`                                                                                                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | Whether the Target is enabled.                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                |
| `server_url`                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | An optional server URL to use.                                                                                                                                                                                                                                                     |

### Response

**[models.UpdateConnectionPolicyTargetResponse](../../models/updateconnectionpolicytargetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_connection_policy_target

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

    sdk.voice_v1_connection_policy_target.delete_connection_policy_target(connection_policy_sid="<id>", sid="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `connection_policy_sid`                                                      | *str*                                                                        | :heavy_check_mark:                                                           | The SID of the Connection Policy that owns the Target.                       |
| `sid`                                                                        | *str*                                                                        | :heavy_check_mark:                                                           | The unique string that we created to identify the Target resource to delete. |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |
| `server_url`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | An optional server URL to use.                                               |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |