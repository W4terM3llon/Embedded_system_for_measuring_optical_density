from machine import Pin

from common.observer import Observer
    

class Blinker(Observer):
    def __init__(self, pinNo):
        super().__init__()
        self.pin = Pin(pinNo, Pin.OUT)
        self.lastBlinkTime = float('-inf')
        self.blinkTimeIntervalInS = 500

    def blinkIfTimeIsRight(self, currentTime):
        if currentTime - self.lastBlinkTime >= self.blinkTimeIntervalInS:
            self.lastBlinkTime = currentTime 
            self.pin.value(not self.pin.value())
            print("Blink")

    def onNotificationReceived(self):
        self.pin.value(0)