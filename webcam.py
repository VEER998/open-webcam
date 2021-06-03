import cv2
import nupy as np

elif 'open camera' in query:
            cap = cv2.VideoCapture(0)

            while True:
                ret, frame = cap.read()
                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xff == ord('c'):
                    break

            cap.realse()
            cv2.destroyAllWindows()
