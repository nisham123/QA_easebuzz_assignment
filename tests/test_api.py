import requests
import time

def test_status_code():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert res.status_code == 200

def test_response_time():
    start = time.time()
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    end = time.time()
    assert (end - start) < 2
