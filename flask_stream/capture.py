import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        # check, frame = self.video.read()
        # cv2.imshow("capturing", frame)
        while True:
            check, frame = self.video.read()
            cv2.imshow("capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break