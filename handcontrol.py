import cv2
import time
import numpy as np
import handtrackingmodule as htm
import math
import subprocess

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

# Volume range for Linux
volMin = 0      # 0%
volMax = 100    # 100%

def set_volume(volume_percent):
    """
    Set the system volume using pactl
    """
    # Ensure it's an integer and clamp between 0-100
    volume_percent = max(0, min(100, int(volume_percent)))
    subprocess.run([
        "pactl",
        "set-sink-volume",
        "@DEFAULT_SINK@",
        f"{volume_percent}%"
    ])

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # Get coordinates of thumb tip and index finger tip
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 7, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)

        # Map hand distance to volume percentage
        # Tune min and max length based on your gestures
        minLength = 30      # fingers almost touching
        maxLength = 150     # fingers far apart

        vol = np.interp(length, [minLength, maxLength], [volMin, volMax])

        # Clamp volume to 0–100 just in case
        vol = max(volMin, min(vol, volMax))
        
        # Set volume
        set_volume(vol)

        # Visual feedback
        cv2.putText(img, f'Volume: {int(vol)}%', (40, 90),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime) if pTime != 0 else 0
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
