from machine import Pin, ADC, PWM
import time

def saveMeasurement(measurement):
    with open("calibratingMeasurements.txt", 'a') as f:
        f.write(f'{measurement}\n')

measurementStartTime = time.time()
measurementLengthInS = 10
measurements = []

#led
a1_pin = ADC(25)
a1_pin.atten(ADC.ATTN_11DB)
a1_pin.width(ADC.WIDTH_12BIT)

pow2_16 = 2**16-1
a2_pin = PWM(Pin(33), freq=100_000, duty_u16=int(8000))
while time.time() - measurementStartTime < measurementLengthInS:
    val = a1_pin.read()
    print(val)
    measurements.append(val)
    time.sleep(0.1)
saveMeasurement(sum(measurements)/len(measurements))        

