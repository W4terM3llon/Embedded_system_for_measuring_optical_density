import requests
import time
import sys

url = 'http://localhost:5000/api/v1/yeastGrowthReadings'
fileName = sys.argv[1]

counter = 0
while True:
    myobj = {'fileName': fileName, 'OD600': counter**2, 'time': counter}
    x = requests.post(url, json=myobj)
    print(f'Sent: {myobj}')
    #print(x.text)
    counter += 1
    time.sleep(0.1)
