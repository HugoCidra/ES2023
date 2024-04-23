#View Manual

## test
-Path: api/REQ6/test/
-Method: POST
-User Authentication: True

Description: Creates a test based on specified tags and returns information about the test's composition.

###Request Format: JSON request body containing the following fields:
```
{
  "tags": ["<str>", "<str>"],
  "title": "<str>"
}
```
-"tags": A list of two tag strings.
-"title": A string representing the title of the test.

###Response Format:
```
{
  "status": 200,
  "message": "Test created successfully",
  "count": {
    "<tag_value>": <int>,
    "<tag_value>": <int>
  }
}
```

-"status": HTTP status code (200 for success).
-"message": A success message.
-"count": A dictionary containing tag counts, where <tag_value> is a tag string, and <int> is the count of questions with that tag in the test.

###Status Codes:

-404: Wrong method.
-400: Invalid credentials.
-401: Unauthorized access.
-200: Success.
--

## tags
-Path: api/REQ6/tags/
-Method: GET
-User Authentication: True

Description: Retrieves a list of tag values from the database.

###Request Format: No request body required.

###Response Format:
```
{
  "status": 200,
  "tags": ["<str>", "<str>", ...]
}
```
-"status": HTTP status code (200 for success).
-"tags": A list of tag values as strings.

###Status Codes:

-404: Wrong method.
-400: Invalid credentials.
-401: Unauthorized access.
-200: Success.
