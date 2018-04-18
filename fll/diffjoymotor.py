######################################################################
# import libraries
######################################################################
from cloudmesh.pi import LCD
from cloudmesh.pi import Joystick
import Adafruit_PCA9685
import time

######################################################################
# lcd set up
######################################################################
lcd = LCD()
lcd.setRGB(255,255,255)

######################################################################
#joystick x + y ranges
#x = -242 to 268
#y = -249 to 241
######################################################################

######################################################################
# set up motor configuration
######################################################################
left = 0
right = 4
middle = 8
min = 480
max = 750
mid = (max - min) / 2 + min
joytoggle = False
click = 0

print "hola"
joy = Joystick()
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(100)
print "Plug motor power in now."
lcd.setText("Plug motor power in now (10 sec).")
time.sleep(1)
lcd.setText("Plug motor power in now (9 sec).")
time.sleep(1)
lcd.setText("Plug motor power in now (8 sec).")
time.sleep(1)
lcd.setText("Plug motor power in now (7 sec).")
time.sleep(1)
lcd.setText("Plug motor power in now (6 sec).")
time.sleep(1)
lcd.setText("Plug motor power in now (5 sec).")
time.sleep(1)
lcd.setText("Plug motor power in now (4 sec).")
time.sleep(1)
lcd.setText("Plug motor power in now (3 sec).")
time.sleep(1)
lcd.setText("Plug motor power in now (2 sec).")
time.sleep(1)
lcd.setText("Plug motor power in now (1 sec).")
time.sleep(1)
lcd.setText("Power should be connected now.")

######################################################################
# start up drone motors
######################################################################

pwm.set_all_pwm(0, 150)
time.sleep(1)
pwm.set_all_pwm(0, 600)
time.sleep(1)

######################################################################
# loop reading joystick and setting values
######################################################################

while True:
	value = joy.get()
	x = value[0]
	y = value[1]
	lastclick = click
	click = value[2]
	if(click == 1):
		x = x -519
	print "The x,y,click values are ", x,y,click
	if(click != lastclick and click == 0):
		joytoggle = not joytoggle 
	print "Joytoggle is ", joytoggle
	if(joytoggle):
		speed = mid
	else:
		speed = min + x
	diff = y - 124
	print "The speed,diff values are ", speed,diff, "(" ,speed + diff,",",speed,",",speed - diff,")"
	#lcd.setText("(" + str(speed + diff) + "," + str(speed) + "," + str(speed - diff)+")")
	pwm.set_pwm(middle,0,speed)
	pwm.set_pwm(left,0,speed + diff)
	pwm.set_pwm(right,0,speed - diff)
	time.sleep(.2)
