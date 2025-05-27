from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    # Match your API response message exactly
    assert response.json() == {"message": "Hand Gesture API running"}

def test_predict_invalid_length():
    invalid_landmarks = [0.0] * 10  # too short input
    response = client.post("/predict", json={"landmarks": invalid_landmarks})
    # Your API currently returns 400 for invalid input length
    assert response.status_code == 400

def test_predict_valid():
    valid_landmarks = [0.0] * 63  # valid length input
    response = client.post("/predict", json={"landmarks": valid_landmarks})
    assert response.status_code == 200
    json_response = response.json()
    assert "prediction" in json_response
    assert isinstance(json_response["prediction"], str)
