import cv2

cap = cv2.VideoCapture(0)

# 해상도 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

print("단축키 안내")
print("  'q' : 종료")
print("  's' : 사진 저장")
print("  'g' : 흑백 전환")

gray_mode = False
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    display = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if gray_mode else frame

    cv2.imshow("Camera", display)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):       # 종료
        break
    elif key == ord('s'):     # 사진 저장
        filename = f"capture_{count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"저장됨: {filename}")
        count += 1
    elif key == ord('g'):     # 흑백 전환
        gray_mode = not gray_mode
        print(f"흑백 모드: {'ON' if gray_mode else 'OFF'}")

cap.release()
cv2.destroyAllWindows()
