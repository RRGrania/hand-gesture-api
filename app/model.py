import joblib
from pathlib import Path

# Paths to the saved model and label encoder files
model_path = Path(__file__).parent.parent / "models" / "optimized_xgboost.pkl"
encoder_path = Path(__file__).parent.parent / "models" / "label_encoder.pkl"

def load_model():
    """
    Load the trained model and label encoder from disk.
    Returns:
        model: The ML model (XGBoost)
        encoder: The label encoder for class labels
    """
    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)
    return model, encoder

# Load model and encoder once when module is imported
model, encoder = load_model()

def predict_gesture(landmarks):
    """
    Predict the hand gesture label given landmarks.
    
    Args:
        landmarks (list or array): List of features (e.g., hand landmarks)
    
    Returns:
        str: Predicted class label
    """
    pred_encoded = model.predict([landmarks])[0]
    label = encoder.inverse_transform([pred_encoded])[0]
    return label
