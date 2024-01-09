from machine import Pin, PWM

class SensorLed:
    def __init__(self, pinNo):    
        self.pin = PWM(Pin(pinNo), freq=100_000, duty_u16=8000)
    