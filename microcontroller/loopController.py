from machine import Pin

from common.observed import Observed

class LoopController(Observed):
    def __init__(self, pinNo):
        super().__init__()
        self.pin = Pin(pinNo, Pin.IN)
        self.isRunning = True
    
    def terminateIfButtonPressed(self):
        if self.pin.value() == 1:
            self.isRunning = False
            self.notifyObservers()
            print("Program terminated")