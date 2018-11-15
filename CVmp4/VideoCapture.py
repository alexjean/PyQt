import cv2

cap = cv2.VideoCapture('d:\mp4\S1E01海底风暴.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('image', frame)
    k = cv2.waitKey(1)
    if k & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()