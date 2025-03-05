# openapi

Developer-friendly & type-safe Python SDK specifically catered to leverage *openapi* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/mr/project). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Twilio - Voice: This is the public Twilio REST API.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [openapi](#openapi)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from openapi python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "openapi",
# ]
# ///

from openapi import SDK

sdk = SDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import dateutil.parser
import openapi
from openapi import SDK

async def main():
    async with SDK(
        security=openapi.Security(
            username="",
            password="",
        ),
    ) as sdk:

        await sdk.voice_v1_archived_call.delete_archived_call_async(date_=dateutil.parser.parse("2024-07-27").date(), sid="<id>")

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                      | Type | Scheme     |
| ------------------------- | ---- | ---------- |
| `username`<br/>`password` | http | HTTP Basic |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [voice_v1_archived_call](docs/sdks/voicev1archivedcall/README.md)

* [delete_archived_call](docs/sdks/voicev1archivedcall/README.md#delete_archived_call) - Delete an archived call record from Bulk Export. Note: this does not also delete the record from the Voice API.

### [voice_v1_bulk_country_update](docs/sdks/voicev1bulkcountryupdate/README.md)

* [create_dialing_permissions_country_bulk_update](docs/sdks/voicev1bulkcountryupdate/README.md#create_dialing_permissions_country_bulk_update) - Create a bulk update request to change voice dialing country permissions of one or more countries identified by the corresponding [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

### [voice_v1_byoc_trunk](docs/sdks/voicev1byoctrunksdk/README.md)

* [create_byoc_trunk](docs/sdks/voicev1byoctrunksdk/README.md#create_byoc_trunk)
* [list_byoc_trunk](docs/sdks/voicev1byoctrunksdk/README.md#list_byoc_trunk)
* [fetch_byoc_trunk](docs/sdks/voicev1byoctrunksdk/README.md#fetch_byoc_trunk)
* [update_byoc_trunk](docs/sdks/voicev1byoctrunksdk/README.md#update_byoc_trunk)
* [delete_byoc_trunk](docs/sdks/voicev1byoctrunksdk/README.md#delete_byoc_trunk)

### [voice_v1_connection_policy](docs/sdks/voicev1connectionpolicysdk/README.md)

* [create_connection_policy](docs/sdks/voicev1connectionpolicysdk/README.md#create_connection_policy)
* [list_connection_policy](docs/sdks/voicev1connectionpolicysdk/README.md#list_connection_policy)
* [fetch_connection_policy](docs/sdks/voicev1connectionpolicysdk/README.md#fetch_connection_policy)
* [update_connection_policy](docs/sdks/voicev1connectionpolicysdk/README.md#update_connection_policy)
* [delete_connection_policy](docs/sdks/voicev1connectionpolicysdk/README.md#delete_connection_policy)

### [voice_v1_connection_policy_target](docs/sdks/voicev1connectionpolicytarget/README.md)

* [create_connection_policy_target](docs/sdks/voicev1connectionpolicytarget/README.md#create_connection_policy_target)
* [list_connection_policy_target](docs/sdks/voicev1connectionpolicytarget/README.md#list_connection_policy_target)
* [fetch_connection_policy_target](docs/sdks/voicev1connectionpolicytarget/README.md#fetch_connection_policy_target)
* [update_connection_policy_target](docs/sdks/voicev1connectionpolicytarget/README.md#update_connection_policy_target)
* [delete_connection_policy_target](docs/sdks/voicev1connectionpolicytarget/README.md#delete_connection_policy_target)

### [voice_v1_country](docs/sdks/voicev1country/README.md)

* [fetch_dialing_permissions_country](docs/sdks/voicev1country/README.md#fetch_dialing_permissions_country) - Retrieve voice dialing country permissions identified by the given ISO country code
* [list_dialing_permissions_country](docs/sdks/voicev1country/README.md#list_dialing_permissions_country) - Retrieve all voice dialing country permissions for this account

### [voice_v1_highrisk_special_prefix](docs/sdks/voicev1highriskspecialprefix/README.md)

* [list_dialing_permissions_hrs_prefixes](docs/sdks/voicev1highriskspecialprefix/README.md#list_dialing_permissions_hrs_prefixes) - Fetch the high-risk special services prefixes from the country resource corresponding to the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

### [voice_v1_ip_record](docs/sdks/voicev1iprecordsdk/README.md)

* [create_ip_record](docs/sdks/voicev1iprecordsdk/README.md#create_ip_record)
* [list_ip_record](docs/sdks/voicev1iprecordsdk/README.md#list_ip_record)
* [fetch_ip_record](docs/sdks/voicev1iprecordsdk/README.md#fetch_ip_record)
* [update_ip_record](docs/sdks/voicev1iprecordsdk/README.md#update_ip_record)
* [delete_ip_record](docs/sdks/voicev1iprecordsdk/README.md#delete_ip_record)

### [voice_v1_settings](docs/sdks/voicev1settings/README.md)

* [fetch_dialing_permissions_settings](docs/sdks/voicev1settings/README.md#fetch_dialing_permissions_settings) - Retrieve voice dialing permissions inheritance for the sub-account
* [update_dialing_permissions_settings](docs/sdks/voicev1settings/README.md#update_dialing_permissions_settings) - Update voice dialing permissions inheritance for the sub-account

### [voice_v1_source_ip_mapping](docs/sdks/voicev1sourceipmappingsdk/README.md)

* [create_source_ip_mapping](docs/sdks/voicev1sourceipmappingsdk/README.md#create_source_ip_mapping)
* [list_source_ip_mapping](docs/sdks/voicev1sourceipmappingsdk/README.md#list_source_ip_mapping)
* [fetch_source_ip_mapping](docs/sdks/voicev1sourceipmappingsdk/README.md#fetch_source_ip_mapping)
* [update_source_ip_mapping](docs/sdks/voicev1sourceipmappingsdk/README.md#update_source_ip_mapping)
* [delete_source_ip_mapping](docs/sdks/voicev1sourceipmappingsdk/README.md#delete_source_ip_mapping)

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import dateutil.parser
import openapi
from openapi import SDK
from openapi.utils import BackoffStrategy, RetryConfig

with SDK(
    security=openapi.Security(
        username="",
        password="",
    ),
) as sdk:

    sdk.voice_v1_archived_call.delete_archived_call(date_=dateutil.parser.parse("2024-07-27").date(), sid="<id>",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Use the SDK ...

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import dateutil.parser
import openapi
from openapi import SDK
from openapi.utils import BackoffStrategy, RetryConfig

with SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=openapi.Security(
        username="",
        password="",
    ),
) as sdk:

    sdk.voice_v1_archived_call.delete_archived_call(date_=dateutil.parser.parse("2024-07-27").date(), sid="<id>")

    # Use the SDK ...

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `delete_archived_call_async` method may raise the following exceptions:

| Error Type      | Status Code | Content Type |
| --------------- | ----------- | ------------ |
| models.APIError | 4XX, 5XX    | \*/\*        |

### Example

```python
import dateutil.parser
import openapi
from openapi import SDK, models

with SDK(
    security=openapi.Security(
        username="",
        password="",
    ),
) as sdk:

    try:

        sdk.voice_v1_archived_call.delete_archived_call(date_=dateutil.parser.parse("2024-07-27").date(), sid="<id>")

        # Use the SDK ...

    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import dateutil.parser
import openapi
from openapi import SDK

with SDK(
    server_url="https://voice.twilio.com",
    security=openapi.Security(
        username="",
        password="",
    ),
) as sdk:

    sdk.voice_v1_archived_call.delete_archived_call(date_=dateutil.parser.parse("2024-07-27").date(), sid="<id>")

    # Use the SDK ...

```

### Override Server URL Per-Operation

The server URL can also be overridden on a per-operation basis, provided a server list was specified for the operation. For example:
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

    sdk.voice_v1_archived_call.delete_archived_call(date_=dateutil.parser.parse("2024-07-27").date(), sid="<id>", server_url="https://voice.twilio.com")

    # Use the SDK ...

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from openapi import SDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from openapi import SDK
from openapi.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import openapi
from openapi import SDK
def main():
    with SDK(
        security=openapi.Security(
            username="",
            password="",
        ),
    ) as sdk:
        # Rest of application here...


# Or when using async:
async def amain():
    async with SDK(
        security=openapi.Security(
            username="",
            password="",
        ),
    ) as sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from openapi import SDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SDK(debug_logger=logging.getLogger("openapi"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python)
