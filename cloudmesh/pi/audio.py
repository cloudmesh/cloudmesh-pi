#!/usr/bin/env python
import sys
import time
import datetime
import paho.mqtt.publish as publish

class Sender(object):

    def __init__(ip="127.0.0.1"):
        self.MQTT_SERVER = ip
        
    def publish_msg(msg = None):
        MQTT_PATH = "audioalert"

        if not msg:
            msg = "Tell me what to say"
        publish.single(MQTT_PATH, msg, hostname=MQTT_SERVER)

def main(msg = None):
    publish_msg(msg)

    
if __name__ == "__main__":
    msg = None
    if len(sys.argv) == 2:
        msg = sys.argv[1]
    main(msg)
