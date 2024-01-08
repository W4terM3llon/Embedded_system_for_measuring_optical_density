from machine import Pin, ADC, PWM
import time
import constants as cnst

class Blinker():
    def __init__(self, pinNo, blinkTimeIntervalInS):
        self.pin = Pin(pinNo, Pin.OUT)
        self.lastBlinkTime = time.ticks_ms()
        self.blinkTimeIntervalInS = blinkTimeIntervalInS

    def blinkIfTimeIsRight(self, currentTime):
        if currentTime - self.lastBlinkTime >= self.blinkTimeIntervalInS:
            self.pin.value(not self.pin.value())
            self.lastBlinkTime = currentTime 


def run():
    blinker = Blinker(26, 500)
    while True:
        currentTime = time.ticks_ms()
        blinker.blinkIfTimeIsRight(currentTime)

run()


