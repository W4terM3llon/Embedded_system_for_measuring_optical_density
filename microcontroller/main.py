import time

from measurement import Measurement
from blinker import Blinker
from sensorLed import SensorLed
from loopController import LoopController
from DataSender import DataSender
        

def run():
    SHOULD_SEND_DATA = True

    measurement = Measurement(15)
    blinker = Blinker(26)

    sensorLed = SensorLed(33)

    loopController = LoopController(34)
    loopController.addObserver(blinker)
    while loopController.isRunning:
        loopController.terminateIfButtonPressed()
        if not loopController.isRunning:
            break

        currentTime = time.ticks_ms()
        measurement.readAndSaveWhenTimeIsRight(currentTime, SHOULD_SEND_DATA)
        blinker.blinkIfTimeIsRight(currentTime)

if __name__ == "__main__":
    run()


