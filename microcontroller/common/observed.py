class Observed():
    def __init__(self):
        self.__observers__ = []

    def addObserver(self, observer):
        self.__observers__.append(observer)

    def notifyObservers(self, ):
        for observer in self.__observers__:
            observer.onNotificationReceived()