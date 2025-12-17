import cv2
import mediapipe as mp
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import math

#pycaw
#grab default speakers
devices = AudioUtilities.GetSpeakers()
interface = devices._dev.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mpDraw = mp.solutions.drawing_utils

#setup webcam
capture = cv2.VideoCapture(0)

while True:
    success, frame = capture.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

            #thumb and pointer tips
            thumb_tip = handLms.landmark[mpHands.HandLandmark.THUMB_TIP]
            index_tip = handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]

            h, w, _ = frame.shape
            x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
            x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

            #draw viz
            cv2.circle(frame, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            #calc pinch distance
            distance = math.hypot(x2 - x1, y2 - y1)

            #convert distance to vol within range of 0.0 - 1.0
            min_dist, max_dist = 20, 200
            vol = max(0.0, min(1.0, (distance - min_dist) / (max_dist - min_dist)))
            volume.SetMasterVolumeLevelScalar(vol, None)

            #display volume level
            cv2.putText(frame, f'Volume: {int(vol * 100)}%', (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('WebcamFeed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()