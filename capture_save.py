import cv2
import os

video = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (600,400))
a = 0

while True:
    a = a+1
    check, frame = video.read()
    print(check)
    print(frame)
    out.write(frame)
    cv2.imshow("capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(a)
video.release()
out.release()
cv2.destroyAllWindows