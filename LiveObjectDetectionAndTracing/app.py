import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from ultralytics import YOLO
import av
import cv2
import os
import time
from datetime import datetime
st.set_page_config(layout="centered")

last_save_time = 0

SAVE_DIR = "detections"
os.makedirs(SAVE_DIR, exist_ok=True)

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

st.title("🎥 Live Object Detection & Tracing")
st.write("Point your camera at objects to identify them in real-time.")

col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    alert_target = st.selectbox("🎯 Target Object:", ["person", "cell phone", "bottle", "keyboard", "laptop", "mouse"])
with col2:
    conf_threshold = st.slider("🔍 Confidence", 0.0, 1.0, 0.5)
with col3:
    enable_save = st.checkbox("💾 Auto-Save", value=False)

def video_frame_callback(frame):
    global last_save_time
    
    img = frame.to_ndarray(format="bgr24")

    results = model.track(
        img,
        persist=True,
        conf=conf_threshold,
        verbose=False
    )

    annotated_frame = results[0].plot()

    obj_count = len(results[0].boxes) if results[0].boxes else 0
    
    cv2.putText(annotated_frame, f"Objects: {obj_count}", (10, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if results[0].boxes:
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            
            if label == alert_target:
                cv2.putText(annotated_frame, f"ALERT: {label.upper()}", (10, 80), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
                current_time = time.time()
                if enable_save and (current_time - last_save_time > 2):
                    timestamp = datetime.now().strftime("%H%M%S")
                    filename = os.path.join(SAVE_DIR, f"alert_{label}_{timestamp}.jpg")
                    cv2.imwrite(filename, annotated_frame)
                    last_save_time = current_time
                break

    return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")

webrtc_streamer(
    key="object-detection",
    mode=WebRtcMode.SENDRECV,
    video_frame_callback=video_frame_callback,
    async_processing=True,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]},
            {"urls": ["stun:stun1.l.google.com:19302"]},
        ]
    },
    media_stream_constraints={
        "video": True,
        "audio": False
    },
)
