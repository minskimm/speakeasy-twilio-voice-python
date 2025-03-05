# VoiceV1BulkCountryUpdate
(*voice_v1_bulk_country_update*)

## Overview

### Available Operations

* [create_dialing_permissions_country_bulk_update](#create_dialing_permissions_country_bulk_update) - Create a bulk update request to change voice dialing country permissions of one or more countries identified by the corresponding [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

## create_dialing_permissions_country_bulk_update

Create a bulk update request to change voice dialing country permissions of one or more countries identified by the corresponding [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

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

    res = sdk.voice_v1_bulk_country_update.create_dialing_permissions_country_bulk_update(request={
        "update_request": "[ { \"iso_code\": \"GB\", \"low_risk_numbers\": \"Enabled\", \"high_risk_special_numbers\":\"Enabled\", \"high_risk_irsf_numbers\": \"Enabled\" } ]",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                     | Type                                                                                                                                                                                                          | Required                                                                                                                                                                                                      | Description                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                     | [models.CreateDialingPermissionsCountryBulkUpdateCreateDialingPermissionsCountryBulkUpdateRequest](../../models/createdialingpermissionscountrybulkupdatecreatedialingpermissionscountrybulkupdaterequest.md) | :heavy_check_mark:                                                                                                                                                                                            | The request object to use for the request.                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                           |
| `server_url`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                            | An optional server URL to use.                                                                                                                                                                                |

### Response

**[models.CreateDialingPermissionsCountryBulkUpdateResponse](../../models/createdialingpermissionscountrybulkupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |