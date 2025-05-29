import os
import joblib
import numpy as np

def load_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'hand-gesture-research'))

    model_path = os.path.join(base_dir, 'gesture_model.pkl')
    encoder_path = os.path.join(base_dir, 'label_encoder.pkl')

    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)

    return model, encoder

def predict_gesture(input_data):
    model, encoder = load_model()
    # assuming input_data is a list or array of features
    input_array = np.array(input_data).reshape(1, -1)  
    pred_encoded = model.predict(input_array)[0]
    pred_label = encoder.inverse_transform([pred_encoded])[0]
    return pred_label