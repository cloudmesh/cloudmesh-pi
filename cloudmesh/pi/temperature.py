from grovepi import *
import time
import smbus
import RPi.GPIO as GPIO


class Temperature(object):
    
    def __init__(self, port=7):
        self.dht_sensor_port = port

    def get(self):    

        try:
            temp, hum = dht(self.dht_sensor_port, 0)
            t = str(temp)
            h = str(hum)
            return t, h
        except (IOError, TypeError) as e:
            print "Error"

if __name__ == "__main__":

    temperature = Temperature()
    while True:
        time.sleep(2)
        print(temperature.get())

