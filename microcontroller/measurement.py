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
        self.measurementsOverTimespanSum = 0
        self.measurementsOverTimespanCount = 0

    def readAndSaveWhenTimeIsRight(self, currentTime):
        od = self.__getCorrectOD__()
        self.measurementsOverTimespanSum += od
        self.measurementsOverTimespanCount += 1
        if currentTime - self.lastMeasurementTime >= self.measurementIntervalInS:
            self.lastMeasurementTime = currentTime 
            averageOd = self.measurementsOverTimespanSum/self.measurementsOverTimespanCount
            with open("measurements.txt", 'a') as file:
                file.write(f"{averageOd}, {(int)(currentTime/1000)}, {self.linesCountOffset + self.fileLinesCount}\n")
                self.fileLinesCount+=1
            print(f"Measurement saved (OD:{averageOd}))")
            self.measurementsOverTimespanSum = 0
            self.measurementsOverTimespanCount = 0
    
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