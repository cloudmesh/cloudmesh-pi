#connect grove button to port D6 of grovepi
#connect grove led bar to port D3 of grovepi
#Run the program
#when you press the button, the level on the led bar increases until it is full
#then it starts again

from cloudmesh.pi import Button
import time
import grovepi

ledbar = 3
grovepi.pinMode(ledbar,"OUTPUT")
grovepi.ledBar_init(ledbar,0)
b = Button(pin=6)

test = 0
while True:
    test += b.get()
    print test
    value = test%11
    print value
    grovepi.ledBar_setLevel(ledbar,value)
    time.sleep(.2)
