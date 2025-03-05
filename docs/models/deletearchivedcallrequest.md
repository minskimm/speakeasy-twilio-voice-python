# DeleteArchivedCallRequest


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `date_`                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)      | :heavy_check_mark:                                                                | The date of the Call in UTC.                                                      |
| `sid`                                                                             | *str*                                                                             | :heavy_check_mark:                                                                | The Twilio-provided Call SID that uniquely identifies the Call resource to delete |