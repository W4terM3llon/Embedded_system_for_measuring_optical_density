import urequests
import network
import time
import json

class DataSender():
    def __init__(self):
        # Define the URL to which you want to send the POST request
        self.url = "http://192.168.195.204:5000/api/v1/yeastGrowthReadings"
        self.fileName = "MicroController.txt"

        self.ssid = 'free_viru5.onion'
        self.password = 'okon3456'
        self.sta_if = network.WLAN(network.STA_IF) # Create a station (STA) interface
        
        self.dataToSendQueue = [] # WARNING !!!storing data can lead to stack overflow and program crashing if sending is slower than reading!!! # Reading has to be done in reasonably large time intervals. 

    def sendMeasurement(self, od, time):
        # "OSError: [Errno 116] ETIMEDOUT: ESP_ERR_TIMEOUT"
        # Apparently, connecting to the network makes pins unsable to read and resuklts in the above exception.
        # Thereforeconenct and disconnect for each request, although very inefficient.
        data = {'fileName': self.fileName, 'OD600': od, 'time': time}        
        print(f"Sending: {data}...")
        self.__connect__()

        self.dataToSendQueue.append(data)
        
        if not self.sta_if.isconnected():
            return
        
        data = self.dataToSendQueue.pop()

        json_data = json.dumps(data)
        response = urequests.post(self.url, data=json_data)
        response.close()

        self.__disconnect__()
        print(f"Sent")

        if len(self.dataToSendQueue) > 0:
            data = self.dataToSendQueue.pop()
            sendMeasurement(data['OD600'], data['time'])


    def __connect__(self):
        print(f'Connecting to Wi-Fi network: {self.ssid}')
        # Activate the interface
        self.sta_if.active(True)
        # Connect to the Wi-Fi network
        self.sta_if.connect(self.ssid, self.password)
        # Wait for the connection to be established
        while not self.sta_if.isconnected():
            time.sleep(1)
        print('Connected to Wi-Fi network')

    def __disconnect__(self):
        self.sta_if.disconnect()
        self.sta_if.active(False)