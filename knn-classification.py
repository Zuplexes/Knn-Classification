import cv2
import numpy as np
import os


def knn(X, y, z, k=1):
    d = np.sum((X - z) ** 2, axis=1)
    idx = np.argsort(d)[:k]
    cls, vote = np.unique(y[idx], return_counts=True)
    return cls[np.argmax(vote)]


X = []
y = []
for name in os.listdir('./'):
    folder = './' + name
    if os.path.isdir(folder):
        for f in os.listdir(folder):
            if f.endswith('.jpg'):
                x = cv2.imread(folder + '/' + f, cv2.IMREAD_GRAYSCALE)
                X.append(x.flatten())
                y.append(name)

X = np.array(X, dtype=np.float32)
y = np.array(y)
if len(X) == 0:
    raise SystemExit('Run GetData.py to save images first.')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    face = cv2.cvtColor(frame[120:300, 250:390, :], cv2.COLOR_BGR2GRAY)
    z = face.flatten().astype(np.float32)
    name = knn(X, y, z)

    cv2.rectangle(frame, (250, 120), (390, 300), (0, 0, 255), 2)
    cv2.putText(frame, str(name), (250, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
