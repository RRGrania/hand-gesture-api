import os
import joblib

def load_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))


    base_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'hand-gesture-research'))

    model_path = os.path.join(base_dir, 'gesture_model.pkl')
    encoder_path = os.path.join(base_dir, 'label_encoder.pkl')

    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)

    return model, encoder
