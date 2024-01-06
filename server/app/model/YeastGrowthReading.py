from datetime import datetime


class YeastGrowthReading():
    def __init__(self, growthIntensity:int, dateTime:datetime):
        self.growthIntensity = growthIntensity
        self.dateTime = dateTime

