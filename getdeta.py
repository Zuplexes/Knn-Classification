import cv2
import os

# รับชื่อโฟลเดอร์จากผู้ใช้ และตรวจสอบการสร้างโฟลเดอร์อัตโนมัติ
name = input("กรุณากรอกชื่อโฟลเดอร์ (Folder Name): ").strip()
if not name:
    name = 'Kritsana'  # กรอกชื่อ

if not os.path.exists(name):
    os.mkdir(name)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

j = 1  # หากต้องการใช้ตัวแปรนับจำนวนภาพ ให้เปลี่ยน i ในภาพเป็น j หรือกำหนด i = 1
i = 1

os.mkdir(name) if not os.path.exists(name) else None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.rectangle(frame, (250, 120), (390, 300), (0, 0, 255), 2)
    face = cv2.cvtColor(frame[120:300, 250:390, :], cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('face', face)

    key = cv2.waitKey(1) & 0xFF

    # ปุ่มกดบันทึกภาพ
    if key == ord('n'):
        cv2.imwrite(f'{name}/{i}.jpg', face)
        print(f"บันทึกภาพที่ {i} ลงโฟลเดอร์ {name} เรียบร้อยแล้ว")
        i += 1

    # ปุ่มสำหรับกดออกจากโปรแกรม (ปุ่ม 'q' หรือ ESC)
    elif key == ord('z') or key == 27:
        print("ปิดโปรแกรม...")
        break

cap.release()
cv2.destroyAllWindows()