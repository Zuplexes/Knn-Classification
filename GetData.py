import cv2
import os

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
name = 'surasek'
os.makedirs('./data/' + name, exist_ok=True)
j = 1

while True:
    ret, frame = cap.read()

    # 1. เช็กความปลอดภัย ป้องกันโปรแกรมแครชหากกล้องอ่านภาพไม่ได้
    if not ret:
        print("ไม่สามารถอ่านภาพจากกล้องได้")
        break

    # 2. Crop ภาพใบหน้าก่อน (เพื่อไม่ให้ติดเส้นสีแดง)
    face = cv2.cvtColor(frame[120:300, 250:390, :], cv2.COLOR_BGR2GRAY)

    # 3. วาดกรอบสี่เหลี่ยมแสดงบนหน้าจอหลัก
    cv2.rectangle(frame, (250, 120), (390, 300), (0, 0, 255), 2)

    cv2.imshow('face', face)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite('./data/' + name + '/' + str(j) + '.jpg', face)
        print(f"save {j} success")
        j += 1
    # 4. เพิ่มปุ่มกด q เพื่อออกจากโปรแกรม
    elif key == ord('q'):
        break

# 5. สั่งปิดกล้องและคืนค่าระบบให้สมบูรณ์
cap.release()
cv2.destroyAllWindows()