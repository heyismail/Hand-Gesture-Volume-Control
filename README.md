# Hand-Gesture-Volume-Control

This Python script utilizes the `mediapipe` library to track hand landmarks and control system volume based on hand gestures. The script detects hand movements using the computer's webcam and adjusts the volume accordingly using the `pyautogui` library.


## Prerequisites

Make sure you have the required libraries installed before running the script:
"pip install opencv-python mediapipe pyautogui"



## Usage

1. Run the script (`hand_volume_control.py`).
"python hand_volume_control.py"

2. The script will open the webcam and track your hand movements.

3. Move your hand up to increase the system volume, and move your hand down to decrease the volume.

4. Press the 'Esc' key to exit the application.



## Dependencies

- OpenCV (`cv2`)
- Mediapipe (`mediapipe`)
- PyAutoGUI (`pyautogui`)



## Notes

- Ensure that your webcam is properly connected and accessible.
- The script assumes the default laptop camera is at index `0`. Adjust the `cv2.VideoCapture(0)` if you are using an external camera.
- The hand gesture for volume control is based on the distance between two specific landmarks on the hand.



Feel free to modify the script based on your preferences or integrate additional features. Enjoy controlling your system volume with hand gestures!
