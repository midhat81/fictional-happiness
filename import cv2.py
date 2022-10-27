import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("ScreenShoot")

img_counter = 0

ret, frame = cam.read()

cv2.imshow("test", frame)

k = cv2.waitKey(1)


# SPACE pressed
img_name = "opencv_frame_{}.png".format(img_counter)
cv2.imwrite(img_name, frame)
print("{} written!".format(img_name))
img_counter += 1
        

cam.release()

cv2.destroyAllWindows()