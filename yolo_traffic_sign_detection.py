from ultralytics import YOLO
import cv2
import os

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')  # Replace with 'best.pt' if you have a custom-trained model

# Define the path to the video file
video_path = r'C:\Users\PMLS\Downloads\TRAFFIC SIGNS.mp4'

# Check if the video file exists
if not os.path.exists(video_path):
    raise FileNotFoundError(f"Video file not found at {video_path}")

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video capture has been initialized correctly
if not cap.isOpened():
    raise IOError(f"Cannot open video file {video_path}")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    results = model(frame)

    # Annotate the frame with detection results
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow('Traffic Sign Detection', annotated_frame)

    # Exit the loop when the ESC key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
