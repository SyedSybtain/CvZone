import cv2

cap = cv2.VideoCapture(1)
output = cv2.VideoWriter("Output.avi",cv2.VideoWriter_fourcc(*'XVID'),10,(1920,1080))

while cap.isOpened():
	timer = cv2.getTickCount()
	ret, img = cap.read()
	if ret is False:
		break
	fps = cv2.getTickFrequency()/(cv2.getTickCount() - timer)
	cv2.putText(img, str(fps), (50,50), cv2.FONT_ITALIC, 1, (0,255,0), 2)
	cv2.imshow("img", img)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
	output.write(img)
cap.release()
output.release()
cv2.destroyAllWindows()

