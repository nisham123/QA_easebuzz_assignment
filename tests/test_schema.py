import requests
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

def test_schema():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = res.json()

    for post in data:
        validate(instance=post, schema=schema)
