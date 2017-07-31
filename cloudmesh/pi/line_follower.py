import time
import grovepi

class lineSensor: #here, we want to have the class to call for the sensor.

    def __init__(self, pin):
        grovepi.pinMode(pin, "INPUT")
        self.line_finder=pin

    def get(self):
        return grovepi.digitalRead(self.line_finder)==1
        #here, we want to have a "get" function that we can call. It should return a "true" bool (or a string, if ya wanna get fancy). d
        

        #here, take the things from the example program to create the conditions for the get function. Lots of it will be copy-and-paste, but use deductive judgement.



        #Good luck!
        
        
