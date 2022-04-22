import cv2

cap = cv2.VideoCapture(0)

while cap.isOpend():
    success, frame = cap.read()
    if success:
        cv2.imShow('Camera Window', frame)

cap.relase()
cv2.destoryAllWindows();