import numpy as np
from app.utils import preprocess_input  # Adjust this import if needed

def test_preprocess_input_valid():
    input_data = [0.1] * 63
    processed = preprocess_input(input_data)
    
    # Check if the output is a numpy array
    assert isinstance(processed, np.ndarray), "Output should be a NumPy array"
    
    # Check the shape of the output
    assert processed.shape == (1, 63), f"Expected shape (1, 63), got {processed.shape}"
