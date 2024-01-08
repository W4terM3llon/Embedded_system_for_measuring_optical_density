from machine import Pin, ADC


class Measurement:
    def __init__(self, pinNo):
        self.a1_pin = ADC(pinNo)
        self.a1_pin.atten(ADC.ATTN_11DB)
        self.a1_pin.width(ADC.WIDTH_12BIT)

        self.linesCountOffset = 1000
        self.fileLinesCount = self.__getFileLinesCount__()

        self.lastMeasurementTime = float('-inf')
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
