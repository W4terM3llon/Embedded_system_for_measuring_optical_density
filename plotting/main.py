import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

def getReadings(fileName):
    readings = []
    with open(fileName, 'r') as f:
        for row in f.readlines():
            readings.append(row.split(', '))
    return readings

def CreateOnePlot(fileName, pngName, title):
    readings = getReadings(fileName)

    adcByDutyNp = np.array(readings, dtype=float)

    plt.scatter(adcByDutyNp[:, 1], adcByDutyNp[:, 0], c="red")

    plt.xlabel('Duty cycle')
    plt.ylabel('ADC')
    plt.title(title)

    plt.savefig(pngName)
    plt.close()

def CreateAIOPlot():
    for i in range(1, 6):
        readings = getReadings(f"data{i}.txt")
        adcByDutyNp = np.array(readings, dtype=float)
        plt.scatter(adcByDutyNp[:, 1], adcByDutyNp[:, 0])

    plt.legend(loc="upper left")

    plt.xlabel('Duty cycle')
    plt.ylabel('ADC')
    plt.title("All in one")

    plt.savefig("dataAIO.png")
    plt.close()


CreateOnePlot("data1.txt", "data1_plot.png", "Resistance: 1Kohm, PEM_freq: 200KHz")
CreateOnePlot("data2.txt", "data2_plot.png", "Resistance: 4Kohm, PEM_freq: 200KHz")
CreateOnePlot("data3.txt", "data3_plot.png", "Resistance: 4Kohm, PEM_freq: 10KHz")
CreateOnePlot("data4.txt", "data4_plot.png", "Resistance: 4Kohm, PEM_freq: 100KHz")
CreateOnePlot("data5.txt", "data5_plot.png", "Resistance: 4Kohm, PEM_freq: 4MHz")
CreateAIOPlot()
