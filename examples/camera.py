######################################################################
# If you do not have pi camera installed run
# 
#     sudo apt-get install python-picamera
#
# You also need to enable camera in raspberrypi configuration
#
# This program uses raspberry pi add-on camera to capture an image and
# after a 5 second countdown timer. 
#
# For more information see
# https://www.raspberrypi.org/documentation/usage/camera/python/README.md
######################################################################
from __future__ import print_function
import picamera
import time

camera = picamera.PiCamera()

count = 5
while count > 0:
    print("capturing image in : ", count)
    count -= 1
    time.sleep(1)

camera.capture("image.jpg")
