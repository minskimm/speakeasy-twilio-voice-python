# CreateSourceIPMappingCreateSourceIPMappingRequest


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `ip_record_sid`                                                                         | *str*                                                                                   | :heavy_check_mark:                                                                      | The Twilio-provided string that uniquely identifies the IP Record resource to map from. |
| `sip_domain_sid`                                                                        | *str*                                                                                   | :heavy_check_mark:                                                                      | The SID of the SIP Domain that the IP Record should be mapped to.                       |