import cv2
import os
import numpy as np

# กำหนดขนาดมาตรฐาน
CROP_W, CROP_H = 240, 300

# 1. อ่านรูปจากโฟลเดอร์พนักงานทุกคนมาเก็บไว้
known_faces = []
known_names = []

dataset_dir = '.'
for folder_name in os.listdir(dataset_dir):
    folder_path = os.path.join(dataset_dir, folder_name)

    if os.path.isdir(folder_path) and not folder_name.startswith('.'):
        for img_name in os.listdir(folder_path):
            if img_name.endswith('.jpg'):
                img_path = os.path.join(folder_path, img_name)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    # บังคับปรับขนาดรูปในฐานข้อมูลให้เป็น 240x300
                    img_resized = cv2.resize(img, (CROP_W, CROP_H))
                    known_faces.append(img_resized)
                    known_names.append(folder_name)

# 2. เปิดกล้องสแกนใบหน้า
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # กรอบใหม่ (200, 80) ถึง (440, 380)
    cv2.rectangle(frame, (200, 80), (440, 380), (0, 0, 255), 2)
    face = cv2.cvtColor(frame[80:380, 200:440, :], cv2.COLOR_BGR2GRAY)

    # บังคับปรับขนาดรูปสดจากกล้องให้เป็น 240x300 เท่ากันเป๊ะ
    face_resized = cv2.resize(face, (CROP_W, CROP_H))

    detected_name = "Unknown"

    if len(known_faces) > 0:
        min_diff = float('inf')
        for idx, k_face in enumerate(known_faces):
            # เปรียบเทียบภาพที่ resize แล้ว
            diff = np.mean((face_resized.astype("float") - k_face.astype("float")) ** 2)
            if diff < min_diff:
                min_diff = diff
                best_match_index = idx

        if min_diff < 4500:
            detected_name = known_names[best_match_index]

    cv2.putText(frame, f"Name: {detected_name}", (200, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('face', face)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()