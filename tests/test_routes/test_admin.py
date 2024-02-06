from fastapi.testclient import TestClient
from app import app
from starlette import status


client = TestClient(app)


def test_create_user():
    request_data = {"username": "test_user", "password": "test_user12@"}
    response = client.post("/v1/users", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED


def test_view_all_user_data():
    response = client.get("v1/users")
    assert response.status_code == status.HTTP_200_OK


def test_view_data_by_user_valid():
    response = client.get("v1/users/user_id/1")
    assert response.status_code == status.HTTP_200_OK


def test_view_data_by_user_invalid():
    response = client.get("v1/users/user_id/2")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_view_user_data_by_website_valid():
    response = client.get("v1/users/website/amazon")
    assert response.status_code == status.HTTP_200_OK


def test_view_user_data_by_website_invalid():
    response = client.get("v1/users/website/flipkart")
    assert response.status_code == status.HTTP_404_NOT_FOUND
