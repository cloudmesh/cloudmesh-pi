import time
import grovepi
from  led import LED

# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button = 3
buzzer = 8
led = 4

grovepi.pinMode(button,"INPUT")
grovepi.pinMode(buzzer, "OUTPUT")
grovepi.pinMode(led, "OUTPUT")


while True:
    if (grovepi.digitalRead(button)):
        grovepi.digitalWrite(led, 1)
        grovepi.digitalWrite(buzzer, 1)
    else:
        grovepi.digitalWrite(led,0)
        grovepi.digitalWrite(buzzer,0)

while True:
    try:
        print(grovepi.digitalRead(button))
        time.sleep(.5)

    except IOError:
        print ("Error")


grove_rgb_lcd.py
# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 8

grovepi.pinMode(buzzer,"OUTPUT")

while True:
    try:
        # Buzz for 1 second
        grovepi.digitalWrite(buzzer,1)
        print ('start')
        time.sleep(1)

        # Stop buzzing for 1 second and repeat
        grovepi.digitalWrite(buzzer,0)
        print ('stop')
        time.sleep(1)

    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
        break
    except IOError:
        print ("Error")



led = LED(3)
t = 0.02
d = 0.01
while t>=d:
    print t
    led.blink(100, t)
    t = t-d
