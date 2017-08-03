import grovepi
import smbus
import time
import sys
import RPi.GPIO as GPIO


class Barometer(object):

    def __init__(self):
        """
        Connect barometer to a I2C port
        """
        # Get I2C bus
        self.bus = smbus.SMBus(1)

    def get(self):
        """
        gets the values of temperature in Celcius and Fahrenheit, and Pressure
        :return: temp_in_C, temp_in_F, preasure
        """

        # BMP280 address, 0x76(118)
        # Read data back from 0x88(136), 24 bytes
        b1 = self.bus.read_i2c_block_data(0x76, 0x88, 24)

        # Convert the data
        # Temp coefficents
        dig_T1 = b1[1] * 256 + b1[0]
        dig_T2 = b1[3] * 256 + b1[2]
        if dig_T2 > 32767 :
            dig_T2 -= 65536
        dig_T3 = b1[5] * 256 + b1[4]
        if dig_T3 > 32767 :
            dig_T3 -= 65536

        # Pressure coefficents
        dig_P1 = b1[7] * 256 + b1[6]
        dig_P2 = b1[9] * 256 + b1[8]
        if dig_P2 > 32767 :
            dig_P2 -= 65536
        dig_P3 = b1[11] * 256 + b1[10]
        if dig_P3 > 32767 :
            dig_P3 -= 65536
        dig_P4 = b1[13] * 256 + b1[12]
        if dig_P4 > 32767 :
            dig_P4 -= 65536
        dig_P5 = b1[15] * 256 + b1[14]
        if dig_P5 > 32767 :
            dig_P5 -= 65536
        dig_P6 = b1[17] * 256 + b1[16]
        if dig_P6 > 32767 :
            dig_P6 -= 65536
        dig_P7 = b1[19] * 256 + b1[18]
        if dig_P7 > 32767 :
            dig_P7 -= 65536
        dig_P8 = b1[21] * 256 + b1[20]
        if dig_P8 > 32767 :
            dig_P8 -= 65536
        dig_P9 = b1[23] * 256 + b1[22]
        if dig_P9 > 32767 :
            dig_P9 -= 65536

        # BMP280 address, 0x76(118)
        # Select Control measurement register, 0xF4(244)
        #		0x27(39)	Pressure and Temperature Oversampling rate = 1
        #					Normal mode
        self.bus.write_byte_data(0x76, 0xF4, 0x27)
        # BMP280 address, 0x76(118)
        # Select Configuration register, 0xF5(245)
        #		0xA0(00)	Stand_by time = 1000 ms
        self.bus.write_byte_data(0x76, 0xF5, 0xA0)

        time.sleep(0.5)

        # BMP280 address, 0x76(118)
        # Read data back from 0xF7(247), 8 bytes
        # Pressure MSB, Pressure LSB, Pressure xLSB, Temperature MSB, Temperature LSB
        # Temperature xLSB, Humidity MSB, Humidity LSB
        data = self.bus.read_i2c_block_data(0x76, 0xF7, 8)

        # Convert pressure and temperature data to 19-bits
        adc_p = ((data[0] * 65536) + (data[1] * 256) + (data[2] & 0xF0)) / 16
        adc_t = ((data[3] * 65536) + (data[4] * 256) + (data[5] & 0xF0)) / 16

        # Temperature offset calculations
        var1 = ((adc_t) / 16384.0 - (dig_T1) / 1024.0) * (dig_T2)
        var2 = (((adc_t) / 131072.0 - (dig_T1) / 8192.0) * ((adc_t ) /131072.0 - (dig_T1 ) /8192.0)) * (dig_T3)
        t_fine = (var1 + var2)
        self.cTemp = (var1 + var2) / 5120.0
        self.fTemp = self.cTemp * 1.8 + 32

        # Pressure offset calculations
        var1 = (t_fine / 2.0) - 64000.0
        var2 = var1 * var1 * (dig_P6) / 32768.0
        var2 = var2 + var1 * (dig_P5) * 2.0
        var2 = (var2 / 4.0) + ((dig_P4) * 65536.0)
        var1 = ((dig_P3) * var1 * var1 / 524288.0 + (dig_P2) * var1) / 524288.0
        var1 = (1.0 + var1 / 32768.0) * (dig_P1)
        p = 1048576.0 - adc_p
        p = (p - (var2 / 4096.0)) * 6250.0 / var1
        var1 = (dig_P9) * p * p / 2147483648.0
        var2 = p * (dig_P8) / 32768.0
        self. pressure = (p + (var1 + var2 + (dig_P7)) / 16.0) / 100

        return self.cTemp, self.fTemp, self.pressure


class Button(object):

    def __init__(self, pin=3):
        """
        Connect button to a digital port. Default is 3.
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(pin,"INPUT")

    def get(self):
        """
        gets the value of the button. 0 if not pressed, 1 if pressed.
        :return: Integer
        """
        return grovepi.digitalRead(self.pin)


class Buzzer(object):

    def __init__(self, pin=3):
        """
        Connect buzzer to a digital port. Default is 3.
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")

    def on(self):
        """
        Turns buzzer on.
        :return: None
        """
        grovepi.digitalWrite(self.pin, 1)  # Send high to switch on buzzer

    def off(self):
        """
        Turns the buzzer off.
        :return: None
        """
        grovepi.digitalWrite(self.pin, 0)  # Send low to switch off buzzer

    def beep(self, n, t=0.2):
        """
        Cycles the buzzer on and off n times with a t second delay. .2 seconds is the default delay.
        :param n: Integer
        :param t: Number
        :return: None
        """
        for i in range(0, n):
            try:
                # on
                self.on()
                time.sleep(t) # duration on
                # off
                self.off()
                time.sleep(t) #duration off

            except KeyboardInterrupt:  # Turn BUZZER off before stopping
                grovepi.digitalWrite(self.pin, 0)
                sys.exit()
                break
            except IOError:  # Print "Error" if communication error encountered
                print ("Error")


class HeartbeatSensor(object):

    def __init__(self):
        """
        Connect to an I2C port.
        """
        rev = GPIO.RPI_REVISION
        if rev == 2 or rev == 3:
            self.bus = smbus.SMBus(1)
        else:
            self.bus = smbus.SMBus(0)
        self.address = 0x50

    def pulse_read(self):
        """
        Returns the heart rate of the wearer.
        :return: Integer
        """
        return self.bus.read_byte(0x50)


class Joystick(object):

    # My Joystick
    #     Min  Typ  Max  Click
    #  X  268  497  755  1020-1023
    #  Y  267  514  756

    # max y = 756
    # min y = 267
    # max x = 755
    # min x = 269

    def __init__(self):
        """
        Connect the Joystick to an analog port. A0 is the default.
        """
        self.xPin = 0
        self.yPin = 1
        grovepi.pinMode(self.xPin, "INPUT")
        grovepi.pinMode(self.yPin, "INPUT")
        self.max_y = 756
        self.min_y = 267
        self.max_x = 755
        self.min_x = 269
        self.typical_x = 498
        self.typical_y = 514

    def get(self):
        """
        gets the x, y, and click status of the joystick
        :return: Integer, Integer, Integer : x, y, click
        """
        try:
            # Get X/Y coordinates
            x = grovepi.analogRead(self.xPin)
            y = grovepi.analogRead(self.yPin)

            # Was a click detected on the X axis?
            click = 1 if x >= 1020 else 0

            print("x =", x, " y =", y, " click =", click)
            x = x - self.typical_x
            y = y - self.typical_y

            if abs(x) <= 1:
                x = 0
            if abs(y) <= 1:
                y = 0
            return x, y, click

        except IOError:
            print ("Error")
            x = 0
            y = 0

    def get_absolute(self):
        """
        gets the difference between the x, y, and click positions and their minimum values
        :return: Number, Number, Number : x, y, click
        """
        try:
            # Get X/Y coordinates
            x = grovepi.analogRead(self.xPin)
            y = grovepi.analogRead(self.yPin)

            # Was a click detected on the X axis?
            click = 1 if x >= 1020 else 0

            print("x =", x, " y =", y, " click =", click)
            return x - self.min_x, y - self.min_y, click

        except IOError:
            print ("Error")
            x = self.typical_x - self.min_x
            y = self.typical_y - self.min_y



class LCD(object):

    def __init__(self):
        """
        connect the LCD screen to an I2C port
        """
        rev = GPIO.RPI_REVISION
        if rev == 2 or rev == 3:
            self.bus = smbus.SMBus(1)
        else:
            self.bus = smbus.SMBus(0)
        # this device has two I2C addresses
        self.DISPLAY_RGB_ADDR = 0x62
        self.DISPLAY_TEXT_ADDR = 0x3e

    def setRGB(self, r,g,b):
        """
        sets the backlight of the LCD to the given values
        :param r: Integer : red
        :param g: Integer : green
        :param b: Integer : blue
        :return: None
        """
        # set backlight to (R,G,B) (values from 0..255 for each)
        self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,0,0)
        self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,1,0)
        self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,0x08,0xaa)
        self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,4,r)
        self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,3,g)
        self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,2,b)

    def textCommand(self, cmd):
        """
        sends a command to LCD
        :param cmd:
        :return: None
        """
        # send command to display (no need for external use)
        self.bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x80,cmd)


    def setText(self, text):
        """
        sets the text on the LCD
        :param text: String
        :return: None
        """
        # set display text \n for second line(or auto wrap)
        self.textCommand(0x01) # clear display
        time.sleep(.05)
        self.textCommand(0x08 | 0x04) # display on, no cursor
        self.textCommand(0x28) # 2 lines
        time.sleep(.05)
        count = 0
        row = 0
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                self.textCommand(0xc0)
                if c == '\n':
                    continue
            count += 1
            self.bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x40,ord(c))

    #Update the display without erasing the display
    def setText_norefresh(self, text):
        """
        sets new text without erasing previous display
        :param text: String
        :return: None
        """
        self.textCommand(0x02) # return home
        time.sleep(.05)

        self.textCommand(0x08 | 0x04) # display on, no cursor
        self.textCommand(0x28) # 2 lines
        time.sleep(.05)
        count = 0
        row = 0
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                self.textCommand(0xc0)
                if c == '\n':
                    continue
            count += 1
            self.bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x40,ord(c))

    def put(self, message):
        """
        sets the text on the display
        :param message: String
        :return: None
        """
        self.setText(message)


class LED(object):

    def __init__(self, pin=3):
        """
        Connect the LED to a digital port. 3 is default.
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")

    def on(self):
        """
        turns LED on.
        :return: None
        """
        grovepi.digitalWrite(self.pin, 1)  # Send HIGH to switch on LED

    def off(self):
        """
        turns LED off.
        :return: None
        """
        grovepi.digitalWrite(self.pin, 0)  # Send LOW to switch off LED

    def blink(self, n, t=0.2):
        """
        blinks LED n times with t time delay. Default t is .2 seconds.
        :param n: Integer
        :param t: Number
        :return: None
        """
        for i in range(0, n):
            try:
                # LED on
                self.on()
                time.sleep(t) # duration on
                # LED off
                self.off()
                time.sleep(t) #duration off

            except KeyboardInterrupt:  # Turn LED off before stopping
                grovepi.digitalWrite(self.pin, 0)
                sys.exit()
                break
            except IOError:  # Print "Error" if communication error encountered
                print ("Error")


class LightSensor(object):

    def __init__(self, pin=0):
        """
        connect to analog port. A0 is default
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(self.pin,"INPUT")

    def get(self):
        """
        returns the sensor value
        :return: Integer
        """
        try:
            return grovepi.analogRead(self.pin)
        except IOError:
            print("Error")


class MoistureSensor(object):

    def __init__(self, pin=0):
        """
        Connect sensor to analog port. A0 is default.
        :param pin: Number
        """
        self.pin = pin

    def get(self):
        return grovepi.analogRead(self.pin)


class Relay(object):

    def __init__(self, pin=4):
        """
        connect relay to digital port. D4 is default.
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")

    def on(self):
        """
        Sets relay on. Allows current to flow.
        :return: None
        """
        try:
            grovepi.digitalWrite(self.pin, 1)
            print('on')
        except IOError:
            print('Error')

    def off(self):
        """
        sets relay off. Stops current flow.
        :return:
        """
        try:
            grovepi.digitalWrite(self.pin, 0)
            print('off')
        except IOError:
            print('Error')

    def put(self, value):
        """
        sets relay to given status. value=0 for off, value=1 for on
        :param value: Integer
        :return: None
        """
        try:
            grovepi.digitalWrite(self.pin, value)
            print(value)
        except IOError:
            print('Error')


class Dendrite(object):

    def __init__(self, pin=4):
        """
        connect to digital pin. default is D4.
        :param pin: Integer
        """
        self.last = None
        self.pin = pin
        self.relay = Relay(pin=self.pin)

    def react_and_wait(self, on=2.5, relax=30):
        """
        causes dendrite to react. current flows for 'on' seconds and relaxes for 'off' seconds.
        :param on: Number
        :param relax: Number
        :return: None
        """
        self.last = time.time()
        self.relay.on()
        time.sleep(on)
        self.relay.off()
        time.sleep(relax)

    def react(self, on=2.5, relax=30):
        """
        causes dendrite to react. current flows for 'on' seconds and relaxes for 'off' seconds.
        Will only react if ready.
        :param on: Number
        :param relax: Number
        :return: None
        """
        if self.ready(relax):
            self.last = time.time()
            self.relay.on()
            time.sleep(on)
            self.relay.off()

    def ready(self, delta=30):
        """
        returns True if dendrite has relaxed for 'delta' seconds. False otherwise. 30 seconds default.
        :param delta: Number
        :return: Boolean
        """
        t = time.time()
        return t - self.last >= delta


class DendriteSwarm(object):

    def __init__(self, pins=[4, 4]):
        """
        dendrite swarm connected to digital ports. D4 and D4 are the defaults.
        :param pins: ListOfIntegers
        """
        self.last = None
        self.pins = pins
        self.relays = []
        for pin in pins:
            self.relays.append(Relay(pin=pin))

    def dance(self, on=2.5, relax=30, delta=[0, 1]):
        """
        causes dendrites to activate for 'on' seconds. all relax for 'relax' seconds.
        stagger reactions by 'delta' seconds.
        :param on: Number
        :param relax: Number
        :param delta: ListOfNumbers
        :return:
        """

        self.last = time.time()

        i = 0
        for relay in self.relays:
            time.sleep(delta[i])
            relay.on()
            i = i + 1

        time.sleep(on)

        i = 0
        for relay in self.relays:
            time.sleep(delta[i])
            relay.off()
            i = i + 1


    def react(self, on=2.5, relax=30):
        """
        All dendrites react. On for 'on' seconds. Relax for 'relax' seconds.
        :param on: Integer
        :param relax: Integer
        :return: None
        """
        if self.ready(relax):
            self.last = time.time()

            for relay in self.relays:
                relay.on()

            time.sleep(on)

            for relay in self.relays:
                relay.off()


    def ready(self, delta):
        """
        returns whether or not the dendrite has relaxed for long enough
        :param delta: Number
        :return: Boolean
        """
        t = time.time()
        if self.last is None:
            return True
        else:
            return t - self.last >= delta


class RotarySensor(object):

    def __init__(self, pin=0):
        """
        connect to analog port. A0 is default.
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "INPUT")
        self.adc_ref = 5
        self.grove_vcc = 5
        self.full_angle = 300

    def get(self):
        """
        gets the value of the rotary sensor.
        :return: Integer
        """
        try:
            return grovepi.analogRead(self.pin)
        except IOError:
            print ("Error")


class Temperature(object):

    def __init__(self, port=7):
        """
        connect to digital port. D7 is default
        :param port: Integer
        """
        self.dht_sensor_port = port

    def get(self):
        """
        gets the temperature and humidity measured by the sensor.
        :return: Number, Number : Temperature, Humidity
        """
        try:
            temp, hum = grovepi.dht(self.dht_sensor_port, 0)
            t = str(temp)
            h = str(hum)
            return t, h
        except (IOError, TypeError) as e:
            print "Error"


class DistanceSensor(object):

    def __init__(self, port=4):
        """
        connect to digital port. D4 is defualt.
        :param port: Integer
        """
        # Connect the Grove Ultrasonic Ranger to digital port D4
        # SIG,NC,VCC,GND
        self.ultrasonic_ranger = port

    def get(self):
        """
        gets the value of the sensor.
        :return: Integer
        """
        return grovepi.ultrasonicRead(self.ultrasonic_ranger)


class WaterSensor(object):

    def __init__(self, pin=2):
        """
        connect sensor to digital port. D2 is default.
        :param pin: Number
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "INPUT")

    def get(self):
        """
        gets the value measured by water sensor.
        :return: Integer
        """
        return grovepi.digitalRead(self.pin)
