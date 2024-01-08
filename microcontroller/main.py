from machine import Pin, ADC, PWM
import time
import constants as cnst


class Observer():
    def onNotificationReceived(self):
        pass

class Observed():
    def __init__(self):
        self.__observers__ = []

    def addObserver(self, observer):
        self.__observers__.append(observer)

    def notifyObservers(self, ):
        for observer in self.__observers__:
            observer.onNotificationReceived()
    

class Blinker(Observer):
    def __init__(self, pinNo):
        super().__init__()
        self.pin = Pin(pinNo, Pin.OUT)
        self.lastBlinkTime = time.ticks_ms()
        self.blinkTimeIntervalInS = 500

    def blinkIfTimeIsRight(self, currentTime):
        if currentTime - self.lastBlinkTime >= self.blinkTimeIntervalInS:
            self.lastBlinkTime = currentTime 
            self.pin.value(not self.pin.value())
            print("Blink")

    def onNotificationReceived(self):
        self.pin.value(0)


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

class MeasurementLight():
    def __init__(self, duty, freq):
        self.duty = duty
        self.freq = freq
        self.a2_pin = PWM(Pin(33), freq=self.freq, duty=self.duty)
        

class Measurement:
    def __init__(self, pinNo):
        self.a1_pin = ADC(pinNo)
        self.a1_pin.atten(ADC.ATTN_11DB)
        self.a1_pin.width(ADC.WIDTH_12BIT)

        self.linesCountOffset = 1000
        self.fileLinesCount = self.__getFileLinesCount__()

        self.lastMeasurementTime = time.ticks_ms()
        self.measurementIntervalInS = 2000

    def readAndSaveWhenTimeIsRight(self, currentTime):
        if currentTime - self.lastMeasurementTime >= self.measurementIntervalInS:
            self.lastMeasurementTime = currentTime 

            #reading = self.a1_pin.read_uv() not used for now
            with open("measurements.txt", 'a') as file:
                file.write(f"{(int)(currentTime/1000)}, {self.linesCountOffset + self.fileLinesCount}\n")
                self.fileLinesCount+=1
            print("Measurement saved")
    
    def __getFileLinesCount__(self):
        try:
            with open("measurements.txt", 'r') as file:
                return len(file.readlines())
        except:#FileNotFoundError
            with open("measurements.txt", 'w') as file:
                return 0


def run():
    measurement = Measurement(25)
    blinker = Blinker(26)
    loopController = LoopController(34)

    loopController.addObserver(blinker)

    while loopController.isRunning:
        loopController.terminateIfButtonPressed()

        currentTime = time.ticks_ms()
        blinker.blinkIfTimeIsRight(currentTime)
        measurement.readAndSaveWhenTimeIsRight(currentTime)

if __name__ == "__main__":
    run()


