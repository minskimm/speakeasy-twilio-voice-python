<!-- Start SDK Example Usage [usage] -->
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