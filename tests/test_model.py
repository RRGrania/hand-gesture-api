from app.model import load_model, predict_gesture

def test_load_model():
    model, encoder = load_model()
    assert model is not None
    assert encoder is not None

def test_predict_gesture():
    # sample input with correct feature size (63 here is your example)
    sample_input = [0.0] * 63  
    prediction = predict_gesture(sample_input)
    assert isinstance(prediction, str)
    model, encoder = load_model()
    known_labels = encoder.classes_.tolist()
    assert prediction in known_labels
