from __future__ import print_function
from guizero import App
from guizero import Slider
from guizero import PushButton
from cloudmesh.pi import Joystick
import Adafruit_PCA9685
import time
import sys

left = 50
right = 50
middle = 50

power = [0, 0, 0]

class Motor(object):
    # 0 = left
    # 1 = middle
    # 2 = right

    def start(self):
        pwm.set_all_pwm(0, 150)
        time.sleep(1)
        pwm.set_all_pwm(0, 600)
        time.sleep(1)

    def warmup(self):
        # warm up motors
        print("Running Motor Warmup")
        pwm.set_all_pwm(0, self.motormax)
        time.sleep(1)
        pwm.set_all_pwm(0, self.motormin)
        time.sleep(1)
        pwm.set_all_pwm(0, self.motormid)
        time.sleep(1)
        pwm.set_all_pwm(0, self.motormin)
        print("Motors ready")
        
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(100)
        
        self.motormin = 520  # was 480
        self.motormax = 750
        self.power = [0,0,0]
        
        # set up motor configuration

        self.left = 0
        self.right = 4
        self.middle = 8
        pins = [self.left, self.right, self.middle]
        
    def set (self, power, motor):
        if power < self.motormmin:
            self.power[motor] = 0
        elif power > self.motormmax:
            self.power[motor] = self.motormax
        else:
            self.power[motor] = power
        pwm.set_pwm(pins[motor], 0, self.power[motor])
        
    def on(self, motor):
        self.set (self.motormax, motor)

    def slow(self, motor):
        self.set (self.motormin, motor)
        
    def off(self, motor, motor)
        self.set (0)

    def setall(self, power)
        self.set(power, 0)
        self.set(power, 2)            
        self.set(power, 1)        

m = Motor()

def do_power(value):
    print(value[0], value[1], value[2])
    m.set(value[0], 0)
    m.set(value[1], 2)            
    m.set(value[3], 1)       

def do_left_button():
    print("Left Button was pressed")
    global m, left, middle, right, power
    power = [0, 0, right]
    do_power(power)


def do_right_button():
    print("Right Button was pressed")
    global m, left, middle, right, power
    power = [left, 0, 0]
    do_power(power)


def do_middle_button():
    print("Middle Button was pressed")
    global left, middle, right, power
    power = [0, middle, 0]
    do_power(power)


def do_forward_button():
    print("Forward Button was pressed")
    global left, middle, right, power
    power = [left, middle, right]
    do_power(power)


def do_stop_button():
    print("Stop Button was pressed")
    global left, middle, right, power
    power = [0, 0, 0]
    do_power(power)


def do_left_slider(value):
    global left, middle, right, power
    print("Left Slider was pressed")
    left = value
    do_power(power)


def do_right_slider(value):
    global left, middle, right, power
    print("Right Slider was pressed")
    right = value
    do_power(power)


def do_middle_slider(value):
    global left, middle, right, power
    print("Middle Button was pressed")
    middle = value
    do_power(power)


app = App(title="Starboat", width=450, height=400, layout="grid")


left_power = Slider(app, command=do_left_slider,
                    grid=[0, 0])
middle_power = Slider(app, command=do_middle_slider,
                      grid=[1, 0])
right_power = Slider(app, command=do_right_slider,
                     grid=[2, 0])
left_power.value = left
right_power.value = right
middle_power.value = middle

leftButton = PushButton(app,
                        image="button-star-trek-left.gif",
                        command=do_left_button, text="Left",
                        grid=[0, 1])
middleButton = PushButton(app,
                          image="button-star-trek-forward.gif",
                          command=do_middle_button, text="Middle",
                          grid=[1, 1])
rightButton = PushButton(app,
                         image="button-star-trek-right.gif",
                         command=do_right_button, text="Right",
                         grid=[2, 1])
forwardButton = PushButton(app,
                           command=do_forward_button, text="Forward",
                           image="button-star-trek-forward.gif",
                           grid=[0, 2])
stopButton = PushButton(app,
                        image="button-star-trek-forward.gif",
                        command=do_stop_button, text="Stop",
                        grid=[2, 2])
stopButton.bg = "red"
forwardButton.bg = "green"

app.display()


#  sips -s format png filename.png --out filename.gif
