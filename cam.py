import cv2

cap = cv2.VideoCapture(0)  # 0 = 기본 웹캠... 하나 더 붙이면 1 씩 늘어나고 뭐 그런거라함 

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

print("카메라 실행 중... 'q' 키를 누르면 종료")

while True:
    ret, frame = cap.read()  # 프레임 읽기

    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    cv2.imshow("Camera", frame)  # 화면에 출력

    if cv2.waitKey(1) & 0xFF == ord('q'):  # q 누르면 종료
        break

cap.release()           # 카메라 해제
cv2.destroyAllWindows() # 창 닫기
