import joblib
from pathlib import Path

model_path = Path(__file__).parent.parent / "models" / "optimized_xgboost.pkl"
encoder_path = Path(__file__).parent.parent / "models" / "label_encoder.pkl"

def load_model():
    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)
    return model, encoder

model, encoder = load_model()
