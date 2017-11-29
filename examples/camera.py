###
# if you dont have picamera installed run sudo apt-get install python-picamera
# and emable camera in raspberrypi configuration
#
#
# this progam uses raspberry pi onboarc camera to capture an image and save it to a file
#
# wait for 5 seconds
# capture the image
# save the mage to image.jpg file
#
# for more information see
# https://www.raspberrypi.org/documentation/usage/camera/python/README.md
###

import picamera
import time

camera = picamera.PiCamera()

count = 5
while count >0:
	print "capturing image in : ", count
	count -= 1
	time.sleep(1)

camera.capture("image.jpg")
