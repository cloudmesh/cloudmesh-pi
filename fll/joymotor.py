from __future__ import print_function
from cloudmesh.pi import Joystick
import Adafruit_PCA9685
import time
print "hola"
joy = Joystick()
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(100)
print "Plug motor power in now."
time.sleep(10)
pwm.set_all_pwm(0, 150)
time.sleep(1)
pwm.set_all_pwm(0, 600)
time.sleep(1)
while True:
	value = joy.get()
	x = value[0]
	print "The x value is ", x
	speed = 600 + x
	pwm.set_all_pwm(0,speed)
	time.sleep(.2)
