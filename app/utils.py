from typing import List
import numpy as np

def preprocess_input(data: List[float]) -> np.ndarray:
    return np.array(data).reshape(1, -1)
