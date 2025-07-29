from ultralytics import YOLO
import cv2

# Load YOLOv8 model (you can use 'yolov8s.pt' or a custom-trained one too)
model = YOLO("yolov8n.pt")  # Or your custom model like "best.pt"

# Correct Windows path with raw string (r"...") to avoid issues with backslashes and spaces
video_path = r"C:\Users\PMLS\Downloads\FOOTBALL VIDEO.mp4"

# Open the football video
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference using YOLOv8
    results = model(frame)

    # Annotate the frame with detection results
    annotated_frame = results[0].plot()

    # Display the result
    cv2.imshow("Football Analysis", annotated_frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
