import matplotlib.pyplot as plt
import numpy as np

def CreatePlot(fileName, pngName, title):
    readings = []
    with open(fileName, 'r') as f:
        for row in f.readlines():
            readings.append(row.split(', '))

    adcByDutyNp = np.array(readings, dtype=int)

    plt.scatter(adcByDutyNp[:, 1], adcByDutyNp[:, 0])

    plt.xlabel('Duty cycle')
    plt.ylabel('ADC')
    plt.title(title)

    plt.savefig(pngName)
    plt.close()

def plotCalibration(fileName, pngName):
    readings = []
    with open(fileName, 'r') as f:
        for row in f.readlines():
            readings.append(row.split(', '))
    readingsNP = np.array(readings, dtype=float)
    i0 = float(readingsNP[0, 0])
    ODArray = readingsNP[1:,:]
    ODArray[:, 0] = np.log10(readingsNP[1:, 0] / i0) * (-1)
    print(np.log10(readingsNP[1:, 0] / i0))

    plt.scatter(ODArray[:, 1], ODArray[:, 0])
    plt.plot([0, 1.25], [0, 1.25])

    plt.savefig(pngName)
    plt.close()

CreatePlot("data1.txt", "data1_plot.png", "Resistance: 1Kohm, PEM_freq: 200KHz")
CreatePlot("data2.txt", "data2_plot.png", "Resistance: 4Kohm, PEM_freq: 200KHz")
CreatePlot("data3.txt", "data3_plot.png", "Resistance: 4Kohm, PEM_freq: 10KHz")
CreatePlot("data4.txt", "data4_plot.png", "Resistance: 4Kohm, PEM_freq: 100KHz")
CreatePlot("data5.txt", "data5_plot.png", "Resistance: 4Kohm, PEM_freq: 4MHz")
CreatePlot("dataX.txt", "dataX_plot.png", ".")

plotCalibration("calibratingMeasurements.txt", "calibratingMeasurements_plot.png")