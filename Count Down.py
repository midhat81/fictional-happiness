# import the time module
import time
from win10toast import ToastNotifier
import cv2
from datetime import datetime

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
date = now.strftime("%Y-%m-%d %H:%M:%S")
date = str(date)
date = date.replace(" ","_")
date = date.replace("-","_")
date = date.replace(":","_")

# define the countdown func.
def countdown(t):
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
# input time in seconds
t = 3
# function call
countdown(int(t))

toaster = ToastNotifier()
toaster.show_toast("Hello World!!!","Python is 10 seconds awsm!", icon_path="custom.ico")
toaster.show_toast("Hello World!!!","Python is awesome by default!")

print('Fire in the hole!!')

cam = cv2.VideoCapture(0)

cv2.namedWindow("ScreenShoot")

img_counter = 0

ret, frame = cam.read()

cv2.imshow("test", frame)

k = cv2.waitKey(1)

img_name = "opencv_"+date+".png"
cv2.imwrite(img_name, frame)





print("{} written!".format(img_name))
img_counter += 1
        

cam.release()

cv2.destroyAllWindows()
