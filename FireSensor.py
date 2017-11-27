#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()
DO = 17
GPIO.setmode(GPIO.BCM)


def setup():
    GPIO.setup(DO, GPIO.IN)


def xprint(x):
    if x == 1:
        lcd.clear()
        lcd.message('All Clear!')
    if x == 0:
        lcd.clear()
        lcd.message('Fire! Run!')


def loop():
    status = 1
    while True:
        tmp = GPIO.input(DO)
        if tmp != status:
            xprint(tmp)
            status = tmp

        time.sleep(0.2)


if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass

