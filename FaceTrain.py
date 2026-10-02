import cv2
import os

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.rectangle(frame, (200,80), (440,380), (0,0,255), 2)

    cv2.putText(
        frame,
        "Press S to save",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):

        name = input("Enter name: ")

        if not os.path.exists(name):
            os.makedirs(name)

        face = frame[80:380, 200:440]

        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        number = len(os.listdir(name)) + 1

        cv2.imwrite(
            f"{name}/{number}.jpg",
            face
        )

        print(f"Saved: {name}/{number}.jpg")

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()