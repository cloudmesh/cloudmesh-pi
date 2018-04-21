from __future__ import print_function
from cloudmesh.pi import Joystick
import Adafruit_PCA9685
import time

print("Starting ...")
joy = Joystick()
pwm = Adafruit_PCA9685.PCA9685()
time.sleep(1)
while True:
    value = joy.get()
    x = value[0]
    y = value[1]
    print("The x,y value is ", x, y)
    time.sleep(.2)
