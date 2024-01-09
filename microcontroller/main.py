import time

from measurement import Measurement
from blinker import Blinker
from sensorLed import SensorLed
from loopController import LoopController
        

def run():
    measurement = Measurement(15)
    blinker = Blinker(26)

    sensorLed = SensorLed(33)

    loopController = LoopController(34)
    loopController.addObserver(blinker)
    while loopController.isRunning:
        loopController.terminateIfButtonPressed()

        currentTime = time.ticks_ms()
        measurement.readAndSaveWhenTimeIsRight(currentTime)
        blinker.blinkIfTimeIsRight(currentTime)

if __name__ == "__main__":
    run()


