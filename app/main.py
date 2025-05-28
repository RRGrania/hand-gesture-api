from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.model import load_model
from app.utils import preprocess_input

# Import Prometheus instrumentator
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Attach Prometheus metrics
Instrumentator().instrument(app).expose(app)

model, encoder = load_model()

class HandLandmarks(BaseModel):
    landmarks: List[float]

@app.get("/")
def root():
    return {"message": "Hand Gesture API running"}

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is healthy"}

@app.get("/labels")
def get_labels():
    return {"labels": list(encoder.classes_)}

@app.post("/predict")
def predict(data: HandLandmarks):
    if len(data.landmarks) != 63:
        raise HTTPException(status_code=400, detail="Invalid number of landmarks, expected 63 floats")
    
    processed_input = preprocess_input(data.landmarks)
    prediction = model.predict(processed_input)
    predicted_label = encoder.inverse_transform(prediction)[0]
    return {"prediction": predicted_label}
