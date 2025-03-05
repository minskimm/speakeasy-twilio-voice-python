# VoiceV1Settings
(*voice_v1_settings*)

## Overview

### Available Operations

* [fetch_dialing_permissions_settings](#fetch_dialing_permissions_settings) - Retrieve voice dialing permissions inheritance for the sub-account
* [update_dialing_permissions_settings](#update_dialing_permissions_settings) - Update voice dialing permissions inheritance for the sub-account

## fetch_dialing_permissions_settings

Retrieve voice dialing permissions inheritance for the sub-account

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

    res = sdk.voice_v1_settings.fetch_dialing_permissions_settings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.FetchDialingPermissionsSettingsResponse](../../models/fetchdialingpermissionssettingsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_dialing_permissions_settings

Update voice dialing permissions inheritance for the sub-account

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

    res = sdk.voice_v1_settings.update_dialing_permissions_settings(request={
        "dialing_permissions_inheritance": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                 | Type                                                                                                                                                                      | Required                                                                                                                                                                  | Description                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                 | [models.UpdateDialingPermissionsSettingsUpdateDialingPermissionsSettingsRequest](../../models/updatedialingpermissionssettingsupdatedialingpermissionssettingsrequest.md) | :heavy_check_mark:                                                                                                                                                        | The request object to use for the request.                                                                                                                                |
| `retries`                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                          | :heavy_minus_sign:                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                       |
| `server_url`                                                                                                                                                              | *Optional[str]*                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                        | An optional server URL to use.                                                                                                                                            |

### Response

**[models.UpdateDialingPermissionsSettingsResponse](../../models/updatedialingpermissionssettingsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |