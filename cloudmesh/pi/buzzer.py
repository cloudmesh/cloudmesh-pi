import time
import grovepi
import sys

class Buzzer(object):

    def __init__(self, pin=3):
        self.pin = pin
        pinMode(self.pin, "OUTPUT")

    def on(self):
        digitalWrite(self.pin, 1)  # Send HIGH to switch on BUZZER

    def off(self):
        digitalWrite(self.pin, 0)  # Send LOW to switch off BUZZER

    def beep(self, n, t=0.2):
        for i in range(0, n):
            try:
                # BUZZER on
                self.on()
                time.sleep(t) # duration on 
                # BUZZER off                
                self.off()
                time.sleep(t) #duration off

            except KeyboardInterrupt:  # Turn BUZZER off before stopping
                digitalWrite(self.pin, 0)
                sys.exit()
                break
            except IOError:  # Print "Error" if communication error encountered
                print ("Error")

if __name__ == "__main__":
    buzzer = BUZZER(pin=3)
    buzzer.beep(5)
    
