import os


def HandleGetMeasurementFileNames():
    return os.listdir(path='./measurements')
