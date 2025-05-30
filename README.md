## 📊 Monitoring Dashboard (Grafana + Prometheus)

To ensure the reliability and performance of the Hand Gesture Recognition API, we've integrated **Prometheus** for metrics collection and **Grafana** for visualization.

### ✅ Key Monitoring Metrics

| Metric Type | Description | Metric Name |
|-------------|-------------|-------------|
| 🧠 Model     | **Garbage Collection Count**: Tracks the frequency of garbage collection events to detect memory inefficiencies that may affect model inference. | `python_gc_collections_total` |
| 📦 Server    | **Resident Memory Usage**: Monitors the live memory usage of the FastAPI server to catch memory bloat or leaks. | `process_resident_memory_bytes` |
| 🔁 Data/API  | **Request Count to `/metrics` Endpoint**: Tracks the number of GET requests made to the Prometheus metrics endpoint. Helps verify Prometheus scraping and API activity. | `http_requests_total` |

### 📷 Dashboard Screenshot

> You can visualize all the above metrics using Grafana.
![WhatsApp Image 2025-05-28 at 16 19 52_6fbebdf7](https://github.com/user-attachments/assets/c8a877c7-4d48-40d0-b1f2-761a8c29763b)
![WhatsApp Image 2025-05-28 at 16 17 01_770ef8ec](https://github.com/user-attachments/assets/0cd3ae5e-d89c-4bb7-ae2f-3a9aa6edfd04)
![WhatsApp Image 2025-05-28 at 14 40 58_410345b5](https://github.com/user-attachments/assets/4b2d14c8-1957-4578-a795-4d70bd6270aa)
![WhatsApp Image 2025-05-28 at 16 19 16_bbd457eb](https://github.com/user-attachments/assets/718c2d61-e260-4401-95a6-da11780f4009)
![WhatsApp Image 2025-05-28 at 15 04 11_9e03d45a](https://github.com/user-attachments/assets/053a516f-7a36-4fbe-951a-1c07b742a213)




---

### 🛠 How It Works

- **Prometheus** scrapes metrics from the API's `/metrics` endpoint (exposed via `prometheus_fastapi_instrumentator`).
- **Grafana** is used to visualize and analyze these metrics in real-time.
- Custom panels are created to show:
  - Python garbage collection events
  - API memory usage
  - Request volume and status codes

---

### 📈 Benefits of Monitoring

- Catch memory issues **before** they crash the app.
- Monitor inference load and adjust resources accordingly.
- Maintain a **healthy API response time** and diagnose 500 errors early.
