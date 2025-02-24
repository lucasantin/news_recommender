import requests

BASE_URL = "http://localhost:5000"

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}

def test_recommend_existing_user():
    payload = {"user_id": "1"}
    response = requests.post(f"{BASE_URL}/recommend", json=payload)
    assert response.status_code == 200
    assert "recommendations" in response.json()


def test_recommend_new_user():
    payload = {"user_id": "99999"}
    response = requests.post(f"{BASE_URL}/recommend", json=payload)
    assert response.status_code == 200
    assert "recommendations" in response.json()


def test_missing_user_id():
    response = requests.post(f"{BASE_URL}/recommend", json={})
    assert response.status_code == 400
    assert "error" in response.json()
