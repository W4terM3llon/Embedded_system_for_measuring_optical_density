import csv


def HandleRecordYeastGrowth(growthIntensity, dateTime):
    with open('YeastGrowthData.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([growthIntensity, dateTime])