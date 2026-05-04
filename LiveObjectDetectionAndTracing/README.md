# Live Object Detection and Tracking

Hey there! This is a project I built to explore the world of Computer Vision. It uses **Streamlit** and **YOLOv8** to detect and track objects through a webcam in real-time. It's pretty snappy because it uses **WebRTC** for low-latency streaming!

## 🌟 What's Cool About This?

- **Real-time Detection:** It catches objects instantly using the latest YOLOv8 model.
- **Smart Tracking:** It doesn't just see things; it follows them around the screen.
- **Target-Specific Alerts & Snapshots:** You can pick a specific object (like a phone) to watch for. If the app sees it, it shows a red alert and can automatically save a screenshot to the `detections/` folder! 📸
- **Interactive Controls:** Use sliders to adjust the AI's confidence levels on the fly without restarting the app.
- **Web-Ready:** Since it's built with WebRTC, it works directly in your browser.

## 🛠️ Built With

- **Python** (The logic)
- **Streamlit** (For the cool dashboard)
- **Ultralytics YOLOv8** (The AI "brain")
- **OpenCV** (For image magic)
- **Streamlit-WebRTC** (For the live camera feed)

## 📋 What You'll Need

- Python 3.10
- A working webcam

## ⚙️ How to Run It

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd LiveObjectDetectionAndTracing
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the app:**
   ```bash
   streamlit run app.py
   ```

Hope you find this as cool as I do! Feel free to reach out if you have ideas on how to improve it.
