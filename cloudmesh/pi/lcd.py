#!/usr/bin/env python
#
# Derived from http://www.seeedstudio.com/wiki/Grove_-_LCD_RGB_Backlight
#


import time,sys
import smbus
import RPi.GPIO as GPIO

class LCD(object):

    def __Init__(self):
        rev = GPIO.RPI_REVISION
        if rev == 2 or rev == 3:
            bus = smbus.SMBus(1)
        else:
            bus = smbus.SMBus(0)
        # this device has two I2C addresses
        DISPLAY_RGB_ADDR = 0x62
        DISPLAY_TEXT_ADDR = 0x3e

    def setRGB(r,g,b):
        # set backlight to (R,G,B) (values from 0..255 for each)
        bus.write_byte_data(DISPLAY_RGB_ADDR,0,0)
        bus.write_byte_data(DISPLAY_RGB_ADDR,1,0)
        bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
        bus.write_byte_data(DISPLAY_RGB_ADDR,4,r)
        bus.write_byte_data(DISPLAY_RGB_ADDR,3,g)
        bus.write_byte_data(DISPLAY_RGB_ADDR,2,b)

    def textCommand(cmd):
        # send command to display (no need for external use)    
        bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)


    def setText(text):
        # set display text \n for second line(or auto wrap)     
        textCommand(0x01) # clear display
        time.sleep(.05)
        textCommand(0x08 | 0x04) # display on, no cursor
        textCommand(0x28) # 2 lines
        time.sleep(.05)
        count = 0
        row = 0
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                textCommand(0xc0)
                if c == '\n':
                    continue
            count += 1
            bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

    #Update the display without erasing the display
    def setText_norefresh(text):
        textCommand(0x02) # return home
        time.sleep(.05)

        textCommand(0x08 | 0x04) # display on, no cursor
        textCommand(0x28) # 2 lines
        time.sleep(.05)
        count = 0
        row = 0
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                textCommand(0xc0)
                if c == '\n':
                    continue
            count += 1
            bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

        def print(self, message):
            self.setText(message)
            
if __name__=="__main__":
    lcd.LCD()
    lcd.setText("Hello world\nCloudmesh.pi")
    lcd.setRGB(0,128,64)
    for c in range(0,255):
        lcd.setRGB(c,255-c,0)
        time.sleep(0.01)
    lcd.setRGB(0,255,0)
    lcd.setText("Bye bye, this should wrap onto next line")
    time.sleep(0.5)
    lcd.print("Hallo")
    
    
