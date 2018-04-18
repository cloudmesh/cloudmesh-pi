#!/usr/bin/env python
import time
import datetime
import paho.mqtt.publish as publish
from cloudmesh.pi import Joystick

def main():
    MQTT_SERVER = "localhost"
    MQTT_PATH = "boatcontrol"

    stick = Joystick()
    while True:
        curTime = datetime.datetime.now()
        (x,y,z) = stick.get()
        #print ("%s|%s|%s" % (x,y,z))
        if int(x)|int(y)|int(z) != 0:
            pubstr = "%s: %s,%s,%s" % (curTime, x, y, z)
            print (pubstr)
            publish.single(MQTT_PATH, pubstr, hostname=MQTT_SERVER)
        time.sleep(0.1)

if __name__ == "__main__":
    main()

