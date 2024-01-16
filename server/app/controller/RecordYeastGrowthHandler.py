def HandleRecordYeastGrowth(fileName, OD600, time):
    with open(f'./measurements/{fileName}', 'a') as f:
        print(f'./measurements/{fileName}')
        f.write(f'{OD600}, {time}, {-1}\n')