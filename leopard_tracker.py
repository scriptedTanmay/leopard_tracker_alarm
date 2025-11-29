from ultralytics import YOLO
import pygame
from PIL import Image
import numpy as np

# Initialize alarm sound
pygame.mixer.init()
pygame.mixer.music.load("alarm.mp3")  # Place alarm.mp3 in same folder

# Load YOLO model (pretrained)
model = YOLO("yolov8n.pt")  # small & fast model

# Open webcam using PIL fallback
import cv2
cap = cv2.VideoCapture(0)

print("Leopard Tracker Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Run YOLO detection
    results = model(frame, verbose=False)

    leopard_detected = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])      # class id
            name = model.names[cls]    # class name

            # YOLO does not have “leopard” class, but it has:
            # "cat", "dog", "bear", "lion", "tiger" depending on model
            if name.lower() in ["cat", "tiger", "lion"]:
                leopard_detected = True

    # Alarm
    if leopard_detected:
        print("⚠️ Leopard-like animal detected!")
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()

    # Display
    cv2.imshow("Leopard Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
