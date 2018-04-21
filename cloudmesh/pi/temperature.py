from grovepi import *
import time
import smbus
import RPi.GPIO as GPIO


class TemperatureSensor(object):
    def __init__(self, port=7):
        """
        connect to digital port. D7 is default
        :param port: Integer
        """
        self.dht_sensor_port = port

    def get(self):
        """
        gets the temperature and humidity measured by the sensor.
        :return: Number, Number : Temperature, Humidity
        """
        try:
            temp, hum = dht(self.dht_sensor_port, 0)
            return str(temp), str(hum)
        except (IOError, TypeError) as e:
            print("Error")

    def __str__(self):
        t, h = temperature.get()
        return "Temperature: {}, Humidity: {}".format(t, h)


if __name__ == "__main__":

    temperature = TemperatureSensor()
    while True:
        time.sleep(2)
        print(temperature.get())
        print(temperature)
