from grove_fingerclip_heart_sensor import *

class HeartbeatSensor(object):
    def __init__(self):
        self.heartbeat = grove_fingerclip_heart_sensor()
        
    def get(self):
        return self.heartbeat.pulse_read()
    
    def getaverage(self, count=10):
        from time import sleep
        storage = []
        
        while count > 0:
            v = self.get()
            if v < 130 and v > 40:
                storage.append(self.get())
                count -= 1
            print("Measured... {}".format(v))
            sleep(0.6)
        
        return sum(storage) / count

        

