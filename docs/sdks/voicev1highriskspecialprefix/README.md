# VoiceV1HighriskSpecialPrefix
(*voice_v1_highrisk_special_prefix*)

## Overview

### Available Operations

* [list_dialing_permissions_hrs_prefixes](#list_dialing_permissions_hrs_prefixes) - Fetch the high-risk special services prefixes from the country resource corresponding to the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

## list_dialing_permissions_hrs_prefixes

Fetch the high-risk special services prefixes from the country resource corresponding to the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

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

    res = sdk.voice_v1_highrisk_special_prefix.list_dialing_permissions_hrs_prefixes(iso_code="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `iso_code`                                                                                                                                                                           | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | The [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to identify the country permissions from which high-risk special service number prefixes are fetched |
| `page_size`                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | How many resources to return in each list page. The default is 50, and the maximum is 1000.                                                                                          |
| `page`                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | The page index. This value is simply for client state.                                                                                                                               |
| `page_token`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | The page token. This is provided by the API.                                                                                                                                         |
| `retries`                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                  |
| `server_url`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | An optional server URL to use.                                                                                                                                                       |

### Response

**[models.ListDialingPermissionsHrsPrefixesResponse](../../models/listdialingpermissionshrsprefixesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |