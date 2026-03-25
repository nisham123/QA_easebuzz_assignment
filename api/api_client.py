import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts():
    response = requests.get(BASE_URL)

    if response.status_code != 200:
        raise Exception("Status code not 200")

    data = response.json()

    for post in data:
        assert "userId" in post
        assert "id" in post
        assert "title" in post
        assert "body" in post

    with open("first_5_posts.json", "w") as f:
        json.dump(data[:5], f, indent=2)

if __name__ == "__main__":
    fetch_posts()
