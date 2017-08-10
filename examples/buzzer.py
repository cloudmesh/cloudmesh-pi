from cloudmesh.pi import Buzzer

if __name__ == "__main__":
    buzzer = Buzzer(pin=3)
    buzzer.beep(5)
