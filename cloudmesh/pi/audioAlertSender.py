#!/usr/bin/env python
import sys
import time
import datetime
import paho.mqtt.publish as publish


def publish_msg(msg=None):
    MQTT_SERVER = "10.0.1.13"
    MQTT_PATH = "cloudmesh/audio"

    if not msg:
        msg = "Tell me what to say"
    publish.single(MQTT_PATH, msg, hostname=MQTT_SERVER)


def main(msg=None):
    publish_msg(msg)


if __name__ == "__main__":
    msg = None
    if len(sys.argv) == 2:
        msg = sys.argv[1]
    main(msg)
