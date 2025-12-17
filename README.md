# 🎚️ VolVision - Gesture-Controlled Volume Adjustment

**VolVision** is a real-time, gesture-based volume controller that uses your webcam to track hand movements. By measuring the distance between your **thumb** and **index finger**, VolVision adjusts your system volume smoothly.

*For Windows*

---

## ✨ Features

- Real-time hand tracking using **MediaPipe**
- Gesture-based system volume control
- Visual feedback overlay:
  - Hand landmarks
  - Pinch-distance line
  - Markers and volume percentage text
- Uses **Pycaw** to control Windows audio
- Lightweight and easy to extend

---

## Under the hood

### MediaPipe Hands
- Detects and tracks hand landmarks in real time
- VolVision extracts:
  - Thumb tip
  - Index finger tip

### OpenCV
- Handles webcam capture
- Draws hand landmarks
- Renders the pinch-distance line
- Displays the current volume percentage

### Pycaw
- Controls the system’s master volume
- Maps pinch distance → volume scalar

### Pinch Logic
- Minimum distance → **0% volume**
- Maximum distance → **100% volume**
- Linear scaling in between




## 📦 Requirements

Install the required Python packages:

```txt
opencv-python==4.10.0.84
mediapipe==0.10.14
pycaw==20230407
comtypes==1.1.14
```
Install them with
```
pip install opencv-python mediapipe pycaw comtypes
```
## Getting started 
before this, get your webcam on and ensure its connected, be ready to get your hand into view.
1. open Powershell in the project directory
2. activate the virtual enviorment for windows (isolated because of dependencies)
```
& .\venv\Scripts\Activate.ps1
```
if successfull it will tuurn into 
```
(venv) your/path/here
```

3. run the application

```
python ./main.py
```
4. press Q to quit

### ⚠️ NOTE: if you are having webcam troubles. this line in main.py may be causing your issue:
```
#setup webcam
capture = cv2.VideoCapture(0)
```
### Camera Index Test Script

If you’re unsure which camera index your webcam uses, run the following script to find the correct one:

```
import cv2

for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera index {i} is available")
        cap.release()
```
Run it with:

```
python test_camera.py

```
Use the index that prints as available and update the specified line accordingly

enjoy! :D