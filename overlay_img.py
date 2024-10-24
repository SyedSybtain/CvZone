import cv2
import cvzone

img_back = cv2.imread(r"C:\Users\ok\Desktop\Python_Codes\car.png", cv2.IMREAD_UNCHANGED)
img_back = cv2.resize(img_back, (10, 50))
video = cv2.VideoCapture(0)
while True:
    success, img = video.read()
    img_new = cvzone.overlayPNG(img1, img_back, pos=[30, 50])
    cv2.imshow("Image", img_new)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
