Leopard Tracker (Python + YOLOv8 + OpenCV)

This project is a real-time Leopard Detection Tool made using Python, YOLOv8, OpenCV, and Pygame. It uses your webcam to detect leopard-like animals such as leopards, tigers, lions, and other big cats. When an animal is detected, the program automatically plays an alarm sound to warn nearby people. Bounding boxes and labels are drawn around detected animals.

This tool can be used for wildlife monitoring, home and farm safety near forest areas, and AI-based animal detection projects. You can also test it by showing a leopard image to the webcam.


---

Features

Real-time webcam detection

Detects leopard-like big cats

Plays alarm sound instantly on detection

Bounding boxes and labels

Easy to install and run

Works on any PC with Python and webcam



---

Installation

1. Install Python 3.8 or above


2. Download or clone this repository


3. Open the project folder in Command Prompt or Terminal


4. Install required libraries using these commands:



pip install ultralytics
pip install opencv-python
pip install pygame

5. Make sure the file alarm.mp3 is placed in the same folder as the Python script.




---

Usage

1. Connect your webcam (or use laptop webcam)


2. Go to the project folder in CMD or Terminal


3. Run the program using:



python leopard_tracker.py

4. The webcam window will open and start detecting animals


5. When a leopard-like animal is detected, the alarm will play automatically


6. Press Q to stop the program




---

Files Included

leopard_tracker.py (main script)

alarm.mp3 (alarm sound file)

README.md

requirements.txt (optional)



---

Important Note

The default YOLOv8 model does not contain a direct “leopard” class, but leopards are detected as similar big cats (cat, lion, tiger, bear), which is still effective for safety alerts.


---

Future Improvements

Custom leopard-trained YOLO model

Telegram/SMS alert system

Image saving when leopard detected

Mobile app version


