import time
import grovepi
from siren import Siren

# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
siren = Siren(4, 8)
button = 3

grovepi.pinMode(button, "INPUT")

while True:
    if grovepi.digitalRead(button):
        siren.start()
    else:
        siren.stop()

while True:
    try:
        print(grovepi.digitalRead(button))
        time.sleep(.5)

    except IOError:
        print("Error")
