import time
import grovepi


class Grove4DigitDisplay(object):
    def __init__(self, pin=5):
        """
        initialize 4 digit display at pin  = 5 by default
        connect to grovePi port D5
        """
        self.display = pin
        grovepi.pinMode(self.display, "OUTPUT")
        grovepi.fourDigit_init(self.display)

    def setBrightness(self, value=0):
        """
        set brightness of the 4 digit display 0 - 8
        brightness set to 0 by default
        """
        grovepi.fourDigit_brightness(self.display, value)

    def setNumber(self, value=0, leading_zero=1):
        """
        display a number on 4 digit display
        by default display number 0 without leading zeroes
        """
        grovepi.fourDigit_number(self.display, value, leading_zero)

    def setDigit(self, position=0, digit=0):
        """
        set a particular digit at a particular position
        position 0 - 3 (0 = leftmost position)
        digit 0 - 15 (0-9A-F)
        by default set digit 0 at position 0
        """
        grovepi.fourDigit_digit(self.display, position, digit)

    def setScore(self, left_score=0, right_score=0):
        """
        display score , i.e two 2 digit values separated by :
        by default display 00:00

        :param left_score:
        :param right_score:
        :return:
        """
        grovepi.fourDigit_score(self.display, left_score, right_score)

    def monitorAnalog(self, pin=0, seconds=0):
        """
        monitor and display the value of an analog pin for some number of seconds
        by default monitor analog pin 0 for 0 seconds
        """
        grovepi.fourDigit_monitor(self.display, pin, seconds)

    def allOn(self):
        """
        switch all lights on
        """
        grovepi.fourDigit_on(self.display)

    def allOff(self):
        """
        switch all lights off
        """
        grovepi.fourDigit_off(self.display)


if __name__ == "__main__":
    print("initialize")
    four_digit_display = Grove4DigitDisplay()
    print("set brightness")
    four_digit_display.setBrightness()
    while True:
        print("set number 5 without leading zeros")
        four_digit_display.setNumber(5, 1)
        time.sleep(0.5)
        print("set number 5 with leading zeros")
        four_digit_display.setNumber(5, 0)
        time.sleep(0.5)
        print("set digits ABCD")
        four_digit_display.setDigit(0, 10)  # A
        four_digit_display.setDigit(1, 11)  # B
        four_digit_display.setDigit(2, 12)  # C
        four_digit_display.setDigit(3, 13)  # D
        time.sleep(0.5)
        print("set score 07:03")
        four_digit_display.setScore(7, 3)
        time.sleep(0.5)
        print("turn all lights on")
        four_digit_display.allOn()
        time.sleep(0.5)
        print("turn all lights off")
        four_digit_display.allOff()
        time.sleep(0.5)
        print("done")
