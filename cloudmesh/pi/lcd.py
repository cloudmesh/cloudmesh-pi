#!/usr/bin/env python
#
# Derived from http://www.seeedstudio.com/wiki/Grove_-_LCD_RGB_Backlight
#


import time,sys
import smbus
import RPi.GPIO as GPIO

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


if __name__=="__main__":
    lcd = LCD()
    lcd.setText("Hello world\nCloudmesh.pi")
    lcd.setRGB(0,128,64)
    for c in range(0,255):
        lcd.setRGB(c,255-c,0)
        time.sleep(0.01)
    lcd.setRGB(0,255,0)
    lcd.setText("Bye bye, this should wrap onto next line")
    time.sleep(0.5)
    lcd.put("Hallo")
    
    
