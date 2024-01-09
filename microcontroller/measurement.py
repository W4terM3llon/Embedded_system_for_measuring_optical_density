from machine import Pin, ADC
import math

import constants as cnst


class Measurement:
    def __init__(self, pinNo):
        self.pin = ADC(pinNo)
        self.pin.atten(ADC.ATTN_11DB)
        self.pin.width(ADC.WIDTH_12BIT)

        self.linesCountOffset = 1000
        self.fileLinesCount = self.__getFileLinesCount__()

        self.lastMeasurementTime = float('-inf')
        self.measurementIntervalInS = 2000

    def readAndSaveWhenTimeIsRight(self, currentTime):
        print(self.__read__())
        if currentTime - self.lastMeasurementTime >= self.measurementIntervalInS:
            self.lastMeasurementTime = currentTime 

            with open("measurements.txt", 'a') as file:
                od = self.__getCorrectOD__()
                file.write(f"{od}, {(int)(currentTime/1000)}, {self.linesCountOffset + self.fileLinesCount}\n")
                self.fileLinesCount+=1
            print("Measurement saved")
    
    def __getFileLinesCount__(self):
        try:
            with open("measurements.txt", 'r') as file:
                return len(file.readlines())
        except:#FileNotFoundError
            with open("measurements.txt", 'w') as file:
                return 0

    def __read__(self):
            reading = self.pin.read_uv()
            return reading
            
    def __getCorrectOD__(self):
            reading = self.__read__()
            od = -math.log10(reading/cnst.ODI0)
            return self.__adjustOdByCalibration__(od)

    def __adjustOdByCalibration__(self, od):
        return (od + 0.0133)/0.6015