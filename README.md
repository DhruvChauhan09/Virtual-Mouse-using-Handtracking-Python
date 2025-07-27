# Virtual Mouse using Hand Tracking
A desktop Virtual Mouse built with Python, OpenCV, MediaPipe, and PyAutoGUI that lets you control your mouse cursor using hand gestures detected from your webcam. Move your index finger to control the cursor, and use a pinch gesture (thumb + index finger) to perform mouse clicks — all without touching your physical mouse.

Features
-Real-time hand tracking using MediaPipe
-Move the cursor with index finger movement
-Pinch gesture to perform left or double-click
-Smooth and accurate cursor mapping
-Works across the screen with configurable sensitivity
-Modular design with a custom hand detection module

Requirements
-Python 3.x
-OpenCV
-MediaPipe
-PyAutoGUI
-NumPy

How to Run
1-Make sure your webcam is working.
2-Run the app.
3-Move your index finger to control the mouse.
4-Pinch your thumb and index finger to click.


How It Works
The app uses MediaPipe to detect 21 hand landmarks from webcam video. It maps the tip of the index finger to your screen coordinates using NumPy interpolation. When the distance between the thumb and index finger is below a threshold, it triggers a mouse click using PyAutoGUI.
