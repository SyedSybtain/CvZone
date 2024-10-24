import cv2
import cvzone

video = cv2.VideoCapture(0)
while True:



    
    t1 = cv2.getTickCount()
    success, img = video.read()
    cvzone.putTextRect(img, "my video", (50, 50))
    cvzone.cornerRect(img, (300, 300, 150, 150))
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-t1)
    cv2.putText(img, str(fps), (100, 100), cv2.FONT_ITALIC, 2, (255, 25, 0), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
