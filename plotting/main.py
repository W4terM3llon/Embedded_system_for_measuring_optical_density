import matplotlib.pyplot as plt
import numpy as np

def CreatePlot(fileName, pngName):
    readings = []
    with open(fileName, 'r') as f:
        for row in f.readlines():
            readings.append(row.split(', '))

    adcByDutyNp = np.array(readings, dtype=int)

    plt.scatter(adcByDutyNp[:, 1], adcByDutyNp[:, 0])

    plt.savefig(pngName)
    plt.close()


CreatePlot("data1.txt", "data1_plot.png")
CreatePlot("data2.txt", "data2_plot.png")
CreatePlot("data3.txt", "data3_plot.png")
CreatePlot("data4.txt", "data4_plot.png")
CreatePlot("data5.txt", "data5_plot.png")
