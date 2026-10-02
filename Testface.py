import cv2
import os
import numpy as np

X = []
y = []

# โหลดรูปจากโฟลเดอร์
for name in os.listdir('.'):
    if name in ['.venv', '.idea']:
        continue

    if not os.path.isdir(name):
        continue

    for file in os.listdir(name):
        img = cv2.imread(f'{name}/{file}', 0)

        if img is not None:
            img = cv2.resize(img, (240, 300))
            X.append(img.flatten())
            y.append(name)

X = np.array(X)
y = np.array(y)

if len(X) == 0:
    print("ไม่พบข้อมูลใบหน้า")
    exit()

# เปิดกล้อง
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # กรอบตรวจใบหน้า
    cv2.rectangle(
        frame,
        (200,80),
        (440,380),
        (0,0,255),
        2
    )

    # ตัดบริเวณใบหน้า
    face = frame[80:380, 200:440]

    # แปลงเป็นขาวดำ
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    # แปลงเป็นข้อมูล
    data = face.flatten()

    # คำนวณ Distance
    d = np.linalg.norm(X - data, axis=1)

    # เลือก 3 คนที่ใกล้ที่สุด
    nearest = np.argsort(d)[:3]

    # นับชื่อที่ซ้ำกัน
    names, counts = np.unique(
        y[nearest],
        return_counts=True
    )

    # หาชื่อที่มีจำนวนมากที่สุด
    result = names[np.argmax(counts)]

    # แสดงชื่อ
    cv2.putText(
        frame,
        result,
        (200,60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0,255,0),
        2
    )

    cv2.imshow(
        "Face Recognition - KNN",
        frame
    )

    # Q = ออกจากโปรแกรม
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()