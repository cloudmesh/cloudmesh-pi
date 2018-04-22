from __future__ import print_function
#import libraries
#from cloudmesh.pi import LCD
from cloudmesh.pi import Joystick
from cloudmesh.pi import LedBar
from cloudmesh.pi import Buzzer
import Adafruit_PCA9685
import time
import sys

def convert100(value , minv,maxv):
	delta = maxv-minv
	newvalue = (value - minv)*(100.0/delta)
	return newvalue

def step100(value):
	if(value<=10):
		return 0
	if(value<20):
		return 20
	if(value<40):
		return 40
	if(value<60):
		return 60
	if(value<80):
		return 80
	return 100

def convert(value, minv, maxv):
	return step100(convert100(value, minv, maxv))

#lcd set up
#lcd = LCD()
#lcd.setRGB(255,255,255)

#joystick x + y ranges
#x = -242 to 268
#y = -249 to 241

#set up motor configuration
wait_time=5
port = 0
starboard = 8
middle = 4
motormin = 520	# was 480
motormax = 750
motortimeout = 30
motordelta = motormax - motormin
motormid = motordelta / 2 + motormin
joytoggle = False
click = 0

print ("hola")

#Initial I/O
ledBar = LedBar(pin=3)
buzzer = Buzzer(pin=2)
joy = Joystick()
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(100)
print ("Plug motor power in now.")
buzzer.beep(3)
for t in range(wait_time,0,-1):
    #lcd.setText("Plug motor power in now ({t} sec).".format(t=t))
    print("Plug motor power in now ({t} sec).".format(t=t))
    ledBar.setLevel(t)
    time.sleep(1)
#lcd.setText("Power should be connected now.")
print ("Power should be connected now.")

#start up drone motors
pwm.set_all_pwm(0, 150)
time.sleep(1)
pwm.set_all_pwm(0, 600)
time.sleep(1)

# warm up motors
print ("Running Motor Warmup")
pwm.set_all_pwm(0, motormax)
time.sleep(1)
pwm.set_all_pwm(0, motormin)
time.sleep(1)
pwm.set_all_pwm(0, motormid)
time.sleep(1)
pwm.set_all_pwm(0, motormin)
print ("Motors ready")


#loop reading joystick and setting values
while True:
	value = joy.get()
	x = value[0]
	y = value[1]
	lastclick = click
	click = value[2]
	if(click == 1):
		x = x -519
	stepx = convert(x, -241, 266)
	stepy = convert(y, -247, 240)
	print ("The corrected stepx,stepy,click values are ", stepx,stepy,click)
	if(click != lastclick and click == 0):
		joytoggle = not joytoggle 
		if(joytoggle):
			stoptime = time.time() + motortimeout
	if(joytoggle and stoptime < time.time()):
		joytoggle = False
		print ("Joytoggle timeout.")
	print ("Joytoggle is ", joytoggle)
	if(joytoggle):
		speed = motormid
	else:
		speed = motormin + (motordelta / 100) * (stepx - 60)
	diff = (stepy - 60) * 3
	print ("The speed,diff values are ", speed,diff, \
		"(" ,speed + diff,",",speed,",",speed - diff,")", \
		joytoggle, time.time(), x, y, stepx, stepy)
	#lcd.setText("(" + str(speed + diff) + "," + str(speed) + "," + str(speed - diff)+")")
	pwm.set_pwm(middle,0,speed)
	pwm.set_pwm(port,0,speed + diff)
	pwm.set_pwm(starboard,0,speed - diff)
	time.sleep(.2)


