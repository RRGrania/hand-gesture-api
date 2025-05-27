from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hand Gesture API is running!"}

def test_predict_valid():
    valid_landmarks = [0.0] * 63  # example dummy data
    response = client.post("/predict", json={"landmarks": valid_landmarks})
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_invalid_length():
    invalid_landmarks = [0.0] * 10  # too short
    response = client.post("/predict", json={"landmarks": invalid_landmarks})
    # Pydantic returns 422 for validation errors
    assert response.status_code == 422
    # Optional: check the validation error details contain length issue
    error_details = response.json()
    assert "detail" in error_details

def test_predict_missing_field():
    response = client.post("/predict", json={})
    assert response.status_code == 422  # Unprocessable Entity, missing required field
