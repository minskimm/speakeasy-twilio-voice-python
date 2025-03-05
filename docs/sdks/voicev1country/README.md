# VoiceV1Country
(*voice_v1_country*)

## Overview

### Available Operations

* [fetch_dialing_permissions_country](#fetch_dialing_permissions_country) - Retrieve voice dialing country permissions identified by the given ISO country code
* [list_dialing_permissions_country](#list_dialing_permissions_country) - Retrieve all voice dialing country permissions for this account

## fetch_dialing_permissions_country

Retrieve voice dialing country permissions identified by the given ISO country code

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

    res = sdk.voice_v1_country.fetch_dialing_permissions_country(iso_code="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `iso_code`                                                                                                                   | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |
| `server_url`                                                                                                                 | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | An optional server URL to use.                                                                                               |

### Response

**[models.FetchDialingPermissionsCountryResponse](../../models/fetchdialingpermissionscountryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_dialing_permissions_country

Retrieve all voice dialing country permissions for this account

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

    res = sdk.voice_v1_country.list_dialing_permissions_country(iso_code="US")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `iso_code`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)                                                                                                              |
| `continent`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Filter to retrieve the country permissions by specifying the continent                                                                                                                                                                         |
| `country_code`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)                                                                                                                                   |
| `low_risk_numbers_enabled`                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                             | Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: `true` or `false`.                                                                                                                                |
| `high_risk_special_numbers_enabled`                                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                             | Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: `true` or `false`                                                                                                                |
| `high_risk_tollfraud_numbers_enabled`                                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                             | Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html) numbers enabled. Can be: `true` or `false`. |
| `page_size`                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | How many resources to return in each list page. The default is 50, and the maximum is 1000.                                                                                                                                                    |
| `page`                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | The page index. This value is simply for client state.                                                                                                                                                                                         |
| `page_token`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | The page token. This is provided by the API.                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                            |
| `server_url`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | An optional server URL to use.                                                                                                                                                                                                                 |

### Response

**[models.ListDialingPermissionsCountryResponse](../../models/listdialingpermissionscountryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |