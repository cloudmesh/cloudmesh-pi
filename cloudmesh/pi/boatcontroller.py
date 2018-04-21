#!/usr/bin/env python
import time
import datetime
import paho.mqtt.publish as publish
from cloudmesh.pi import Joystick


def main():
    MQTT_SERVER = "localhost"
    MQTT_PATH = "boatcontrol"

    stick = Joystick()
    prevxy = [0, 0]
    while True:
        curTime = datetime.datetime.now()
        (x, y, z) = stick.get_scaled()
        # print ("%s|%s|%s" % (x,y,z))
        if int(x) | int(y) | int(z) != 0:
            pubstr = "%s: %s,%s,%s" % (curTime, x, y, z)
            print(pubstr)
            # filter out abrupt/false click probably due to EMI
            # only publish the REAL ones if we found two consecutive valid coordinate changes within 0.1 second
            if x * prevxy[0] != 0 or y * prevxy[1] != 0:
                publish.single(MQTT_PATH, pubstr, hostname=MQTT_SERVER)
        prevxy[0] = x
        prevxy[1] = y
        time.sleep(0.1)


if __name__ == "__main__":
    main()
