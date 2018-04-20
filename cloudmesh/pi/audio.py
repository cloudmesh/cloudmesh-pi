#!/usr/bin/env python
import sys
import time
import datetime
import os
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
 
class Publisher(object):

    def __init__(self, ip="127.0.0.1", path="cloudmesh/audio"):
        self.MQTT_SERVER = ip
        self.MQTT_PATH = path
        
    def send(sef, msg = None):
        if not msg:
            msg = "Tell me what to say"
        publish.single(self.MQTT_PATH,
                       msg,
                       hostname=self.MQTT_SERVER)


class Receiver(object):

    def __init__(self, ip="127.0.0.1", path="cloudmesh/audio"):
        self.MQTT_SERVER = ip
        self.MQTT_PATH = path
    
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
 
        # Subscribing in on_connect() means that if we lose the
        # connection and reconnect then subscriptions will be renewed.
        client.subscribe(self, self.MQTT_PATH)
 
    # The callback for when a PUBLISH message is received from the server.
    def on_message(self.client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        os.system("say '%s'" % msg.payload)
        # more callbacks, etc

    def run()
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
 
        client.connect(self.MQTT_SERVER, 1883, 60)
 
        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()

        
"""

PUBLISHER: Define an aexample elsewhere, 
        
def main(msg = None):
    p = Publisher(ip="10.0.0.13")
    p.send(msg)

    
if __name__ == "__main__":
    msg = None
    if len(sys.argv) == 2:
        msg = sys.argv[1]
    main(msg)

"""

"""
# RECEIVER: DEFINE ELSEWHERE
r = Reciever()
r.run()
"""
