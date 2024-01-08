from machine import Pin, ADC, PWM
import time

<<<<<<< Updated upstream
=======
def saveMeasurement(measurement):
    with open("calibratingMeasurements.txt", 'a') as f:
        f.write(f'{measurement}\n')

measurementStartTime = time.time()
measurementLengthInS = 10
measurements = []

#led
>>>>>>> Stashed changes
a1_pin = ADC(25)
a1_pin.atten(ADC.ATTN_11DB)
a1_pin.width(ADC.WIDTH_12BIT)

pow2_16 = 2**16-1
<<<<<<< Updated upstream
pow2_12 = 2**12-1
a2_pin = PWM(Pin(33), freq=4_000_000, duty_u16=0)

dutyIncrement=50
over1000Counter = 0
with open('data5.txt','w') as file:
    duty = 0
    while True:
        a2_pin.duty_u16(duty)
        reading = a1_pin.read_uv()
        print(reading)

        duty = duty+dutyIncrement

        file.write(f"{reading}, {duty}\n")
        time.sleep(0.0001)
        
        if reading >= pow2_12:
            over1000Counter+=1
        
        if reading >= pow2_12 and over1000Counter > 100:
            break
=======
a2_pin = PWM(Pin(33), freq=100_000, duty_u16=int(8000))
while time.time() - measurementStartTime < measurementLengthInS:
    val = a1_pin.read()
    print(val)
    measurements.append(val)
    time.sleep(0.1)
saveMeasurement(sum(measurements)/len(measurements))        
            


#import machine
#machine.reset()
>>>>>>> Stashed changes


