# API Documentation

## Label Settings Endpoint

### GET /v1/label-settings

Retrieve a list of label configurations and settings.

#### Query Parameters

- `page`: The page number for pagination.
- `per_page`: The number of items per page.
- `default`: Filter labels by default state (true/false).
- `category`: Filter labels by category.

#### Response

Returns a JSON object with label details, pagination info, and total count.
