from cloudmesh.pi import Button
import time

if __name__ == "__main__":

    button = Button(pin=3)

    while True:
        try:
            print(button.get())
            time.sleep(.5)
        except IOError:
            print ("Error")


