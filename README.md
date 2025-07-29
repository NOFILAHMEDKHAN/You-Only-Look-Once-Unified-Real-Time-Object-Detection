# ⚽🚦 Real-Time Object Detection using YOLOv8

🎯 Objective  
To perform real-time object detection using the YOLOv8 model in Python with Ultralytics. This lab includes:

- Detecting and localizing traffic signs from video files  
- Analyzing football match footage to detect players and objects  
- Applying YOLOv8 with OpenCV for live annotation and visualization  

---

📁 Code Files  

🔹 `yolo_traffic_sign_detection.py`  
This script performs object detection on a traffic sign video using the YOLOv8 model.

📌 Key Components:  
Model: `yolov8n.pt` (Ultralytics pretrained lightweight YOLO model)  
Input: Traffic video file (`.mp4`)  
Detection: YOLOv8's `.predict()` used on each frame  
Visualization: Bounding boxes drawn with `results[0].plot()`  
Interface: OpenCV used to display annotated video frame-by-frame  

📈 Output:  
- Bounding boxes on traffic signs in real-time  
- Displayed in a video window using OpenCV  
- Stops on pressing the **ESC** key  

🔹 `yolo_football_analysis.py`  
This script analyzes a football video using YOLOv8 to detect players and other elements in the scene.

📌 Key Components:  
Model: `yolov8n.pt` or a custom model like `best.pt`  
Input: Football video file  
Detection: Each frame passed to YOLO and processed  
Visualization: Draws boxes on detected players and objects  
Interface: Output shown frame-by-frame using OpenCV  

📈 Output:  
- Annotated football video with live detections  
- Player/object tracking shown using bounding boxes  
- Ends on ESC key press  

---

🧰 Requirements  
Install dependencies using:

```bash
pip install ultralytics opencv-python
🔁 How to Run:

For traffic sign detection:

bash
Copy
Edit
python yolo_traffic_sign_detection.py
For football video analysis:

bash
Copy
Edit
python yolo_football_analysis.py
✅ Ensure you set correct video paths in the scripts:

python
Copy
Edit
video_path = r"C:\Users\YourName\Videos\traffic.mp4"
video_path = r"C:\Users\YourName\Videos\football.mp4"
📌 Notes:

YOLOv8 offers real-time performance and high accuracy

yolov8n.pt is lightweight and ideal for CPU-based detection

For better accuracy, use yolov8s.pt, yolov8m.pt, or your own best.pt

Exits cleanly with ESC key during playback

Easily extendable to detect custom classes like referees, balls, road signs, etc.

yaml
Copy
Edit
