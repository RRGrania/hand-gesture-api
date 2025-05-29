import os
import joblib
import numpy as np

def load_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, 'models', 'gesture_model.pkl')
    encoder_path = os.path.join(current_dir, 'models', 'label_encoder.pkl')

    print(f"Looking for model at: {model_path}")
    print(f"Looking for encoder at: {encoder_path}")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    if not os.path.exists(encoder_path):
        raise FileNotFoundError(f"Encoder file not found at {encoder_path}")

    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)
    return model, encoder


def predict_gesture(input_data):
    model, encoder = load_model()
    
    # Ensure input_data is numpy array and reshaped correctly for prediction
    input_array = np.array(input_data).reshape(1, -1)
    
    # Predict encoded label
    pred_encoded = model.predict(input_array)[0]
    
    # Decode to actual label string
    pred_label = encoder.inverse_transform([pred_encoded])[0]
    
    return pred_label
