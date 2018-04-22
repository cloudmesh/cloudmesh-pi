from __future__ import print_function
from cloudmesh.pi import Joystick
import Adafruit_PCA9685
import time

print("Starting ...")
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(100)
for t in range(5, 0, -1):
    print("Plug motor power in now.", t, "seconds left")
    time.sleep(1)

time.sleep(3)
    
pwm.set_all_pwm(0, 150)
time.sleep(1)
pwm.set_all_pwm(0, 600)
time.sleep(1)


pwm.set_all_pwm(0, 700)
time.sleep(2)
