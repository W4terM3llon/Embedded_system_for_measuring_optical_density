import csv
import io

from matplotlib import use as mtplUse
import matplotlib.pyplot as plt
import numpy as np

from app.model.YeastGrowthReading import YeastGrowthReading


def HandleGetYeastGrowthImage():
    data = np.array(ReadDataFromFileAsLists("YeastGrowthData.csv"))
    graphAsBytes = RenderPlot(data)
    return graphAsBytes


def RenderPlot(data) -> bytes:
    mtplUse('SVG')

    plt.xlabel("Light intensity")
    plt.ylabel("Time")
    plt.title("Yeast growth")

    fig, ax = plt.subplots()
    plt.xticks(rotation=45, ha='right')
    ax.plot(data[:, 1], data[:, 0])

    # save as a file just in case
    plt.savefig('YeastGrowth.png', format="png")

    image_bytes = io.BytesIO()
    plt.savefig(image_bytes, format="png")
    image_bytes.seek(0)

    return image_bytes.read()


def ReadDataFromFileAsLists(path):
    return [[obj.growthIntensity, obj.dateTime] for obj in ReadDataFromFileAsObjects(path)]

def ReadDataFromFileAsObjects(path) -> list[YeastGrowthReading]:
    result = []
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                result.append(YeastGrowthReading(row[0], row[1]))
    except FileExistsError:
        return []
    return result