import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.parametrize("endpoint", ["/posts", "/comments", "/users"])
def test_endpoints(endpoint):
    res = requests.get(BASE_URL + endpoint)
    assert res.status_code == 200
