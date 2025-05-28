# Hand Gesture Recognition API

This project provides a FastAPI-based REST API for recognizing hand gestures using a pre-trained machine learning model.

---

## Features

- Predict hand gestures from 21 hand landmarks (63 float values)
- Health check endpoint
- Retrieve list of gesture labels
- Dockerized for easy deployment


## Monitoring Metrics

1. **Model Metric:** Inference time (measured in milliseconds)
   - Helps track performance regressions.

2. **Data Metric:** Distribution of input lengths
   - Ensures consistency in data passed to the model.

3. **Server Metric:** API latency (ms) and number of 500 errors
   - Detects backend/server issues.

Logged using Prometheus + Grafana.

