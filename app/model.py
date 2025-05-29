import os
import joblib
import numpy as np

def load_model():
    # Get the directory of this file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Adjust this path to where your model files really are, relative to current_dir
    base_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'hand-gesture-research'))
    
    model_path = os.path.join(base_dir, 'gesture_model.pkl')
    encoder_path = os.path.join(base_dir, 'label_encoder.pkl')
    
    # Debug prints to help troubleshooting path issues
    print(f"Looking for model at: {model_path}")
    print(f"Looking for encoder at: {encoder_path}")
    
    # Check that files exist
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    if not os.path.exists(encoder_path):
        raise FileNotFoundError(f"Encoder file not found at {encoder_path}")
    
    # Load model and encoder
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
