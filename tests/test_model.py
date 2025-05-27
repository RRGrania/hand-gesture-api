from app.model import load_model, predict_gesture

def test_load_model():
    model, encoder = load_model()
    assert model is not None
    assert encoder is not None

def test_predict_gesture():
    model, encoder = load_model()
    sample_input = [0.0] * 63  # example dummy input with correct length
    prediction = predict_gesture(sample_input)
    assert isinstance(prediction, str)
    known_labels = encoder.classes_.tolist()  # get all known labels from encoder
    assert prediction in known_labels
