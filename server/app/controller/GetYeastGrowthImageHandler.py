import io

from matplotlib import use as mtplUse
import matplotlib.pyplot as plt
import numpy as np


def HandleGetYeastGrowthImage(name):
    with open(f'./measurements/{name}', 'r') as f:
        lines = f.readlines()
        data = np.empty((len(lines), 2))
        for i in range(len(lines)):
            variables = lines[i].split(', ')
            data[i, :] = [variables[0], variables[1]]

    mtplUse('SVG')


    fig, ax = plt.subplots()
    plt.xlabel("Time (h)")
    plt.ylabel("OD600")
    plt.title(f"Yeast growth ({name[:-4]})")
    plt.xticks(rotation=45, ha='right')
    ax.plot(data[:, 1]/3600, data[:, 0])

    # save as a file just in case
    plt.savefig('YeastGrowth.png', format="png")

    image_bytes = io.BytesIO()
    plt.savefig(image_bytes, format="png")
    image_bytes.seek(0)

    return image_bytes.read()