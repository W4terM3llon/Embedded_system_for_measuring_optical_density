from machine import Pin, ADC
import math

import constants as cnst
from DataSender import DataSender


class Measurement:
    def __init__(self, pinNo):
        self.pin = ADC(pinNo)
        self.pin.atten(ADC.ATTN_11DB)
        self.pin.width(ADC.WIDTH_12BIT)

        self.linesCountOffset = 1000
        self.fileLinesCount = 0

        self.lastMeasurementTime = float('-inf')
        self.measurementIntervalInS = 10*1000
        self.measurementsOverTimespanSum = 0
        self.measurementsOverTimespanCount = 0

        self.dataSender = DataSender()

    def readAndSaveWhenTimeIsRight(self, currentTime, shouldSendData):
        od = self.__getCorrectOD__()
        self.measurementsOverTimespanSum += od
        self.measurementsOverTimespanCount += 1
        if currentTime - self.lastMeasurementTime >= self.measurementIntervalInS:
            self.lastMeasurementTime = currentTime 
            averageOd = self.measurementsOverTimespanSum/self.measurementsOverTimespanCount
            time = (int)(currentTime/1000)
            id = self.linesCountOffset + self.fileLinesCount
            if shouldSendData:
                self.dataSender.sendMeasurement(averageOd, time)
            with open("measurements.txt", 'a') as file:
                file.write(f"{averageOd}, {time}, {id}\n")
                self.fileLinesCount+=1
            print(f"Measurement saved (OD:{averageOd}))")
            self.measurementsOverTimespanSum = 0
            self.measurementsOverTimespanCount = 0

    def __read__(self):
        return self.pin.read_uv()
            
    def __getCorrectOD__(self):
        reading = self.__read__()
        od = -math.log10(reading/cnst.ODI0)
        return self.__adjustOdByCalibration__(od)

    def __adjustOdByCalibration__(self, od):
        return (od + 0.0133)/0.6015