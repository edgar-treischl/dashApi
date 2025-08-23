from fastapi.testclient import TestClient
from dashApi.main import app

client = TestClient(app)

def test_hello():
    r = client.get("/hello?name=Jane")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, Jane!"}
