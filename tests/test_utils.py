import numpy as np
from app.utils import preprocess_input  # adjust import if your utils file is named differently

def test_preprocess_input_valid():
    input_data = [0.1] * 63
    processed = preprocess_input(input_data)
    # Assuming preprocess_input returns a numpy array shaped (1, 63)
    assert isinstance(processed, np.ndarray)
    assert processed.shape == (1, 63)
