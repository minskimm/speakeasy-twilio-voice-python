# VoiceV1ArchivedCall
(*voice_v1_archived_call*)

## Overview

### Available Operations

* [delete_archived_call](#delete_archived_call) - Delete an archived call record from Bulk Export. Note: this does not also delete the record from the Voice API.

## delete_archived_call

Delete an archived call record from Bulk Export. Note: this does not also delete the record from the Voice API.

### Example Usage

```python
import dateutil.parser
import openapi
from openapi import SDK

with SDK(
    security=openapi.Security(
        username="",
        password="",
    ),
) as sdk:

    sdk.voice_v1_archived_call.delete_archived_call(date_=dateutil.parser.parse("2024-07-27").date(), sid="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `date_`                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)      | :heavy_check_mark:                                                                | The date of the Call in UTC.                                                      |
| `sid`                                                                             | *str*                                                                             | :heavy_check_mark:                                                                | The Twilio-provided Call SID that uniquely identifies the Call resource to delete |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |
| `server_url`                                                                      | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | An optional server URL to use.                                                    |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |