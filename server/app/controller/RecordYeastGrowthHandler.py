def HandleRecordYeastGrowth(fileName, OD600, time):
    with open(f'./measurements/{fileName}', 'a') as f:
        f.write(f'{OD600}, {time}, {-1}\n')