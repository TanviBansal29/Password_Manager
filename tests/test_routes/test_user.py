from fastapi.testclient import TestClient
from app import app
from utils.tokens import get_jwt
from starlette import status

client = TestClient(app)


# Mocking
def override_user_dependency():
    return {"fresh": True, "iat": "1234", "type": "access", "sub": "1", "exp": "12345"}


app.dependency_overrides[get_jwt] = override_user_dependency


def test_add_data():
    request_data = {
        "username": "tbansal@12",
        "website": "netflix",
        "email": "tanvi2020bansal12@gmail.com",
        "password": "netflixtanvi2@",
    }
    response = client.post("v1/users/data", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED


def test_view_all_data():
    print("hello")
    response = client.get("/v1/users/mydata")
    assert response.status_code == status.HTTP_200_OK


def test_view_data_by_website_valid():
    response = client.get("v1/users/mydata/website/amazon")
    assert response.status_code == status.HTTP_200_OK


def test_view_data_by_website_invalid():
    response = client.get("v1/users/mydata/website/flipkart")
    assert response.status_code == status.HTTP_404_NOT_FOUND
