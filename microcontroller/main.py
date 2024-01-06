from machine import Pin, ADC, PWM
import time

a1_pin = ADC(25)
a1_pin.atten(ADC.ATTN_11DB)
a1_pin.width(ADC.WIDTH_10BIT)

pow2_16 = 2**16-1
a2_pin = PWM(Pin(33), freq=4_000, duty_u16=0)

def saveReading(data):
    with open("sensorReadings.csv", 'a') as f:
        f.write(data)
        f.write("\n")

duty = 0
while True:
    a2_pin.duty_u16(duty)
    reading = a1_pin.read_uv()
    saveReading(reading)
    print(reading)

    duty = duty+100
    time.sleep(0.1)
    if duty > pow2_16:
        break


