from cloudmesh.pi import LCD
from cloudmesh.pi import TemperatureSensor
import time

lcd = LCD()
lcd.setRGB(255, 255, 255)
temp = TemperatureSensor()

while True:
    t, h = temp.get()
    lcd.setText("Temperature:" + str(t) + "Humidity:" + str(h))
    time.sleep(2)
