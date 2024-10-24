import cv2
import cvzone

video = cv2.VideoCapture(0)
while True:
    success, img = video.read()
    stacked_img = cvzone.stackImages([img, img, img, img, img, img, img, img, img], 3, 0.5)
    cv2.imshow("Image", stacked_img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
