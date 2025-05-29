import pandas as pd

def preprocess_input(landmarks: list):
    if len(landmarks) != 63:
        raise ValueError("Input must be 63 floats")
    cols = []
    for i in range(1, 22):
        cols += [f'x{i}', f'y{i}', f'z{i}']
    df_input = pd.DataFrame([landmarks], columns=cols)

    wrist_x = df_input.loc[0, 'x1']
    wrist_y = df_input.loc[0, 'y1']
    wrist_z = df_input.loc[0, 'z1']

    for i in range(1, 22):
        df_input[f'x{i}'] -= wrist_x
        df_input[f'y{i}'] -= wrist_y
        df_input[f'z{i}'] -= wrist_z

    max_val = df_input.abs().max(axis=1).values[0] + 1e-8
    for col in cols:
        df_input[col] /= max_val

    return df_input
