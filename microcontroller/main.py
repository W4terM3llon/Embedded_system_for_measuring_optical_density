from machine import Pin, ADC, PWM
import time

a1_pin = ADC(25)
a1_pin.atten(ADC.ATTN_11DB)
a1_pin.width(ADC.WIDTH_10BIT)

pow2_16 = 2**16-1
a2_pin = PWM(Pin(33), freq=10_000, duty_u16=0)


over1000Counter = 0
with open('data222.txt','w') as file:
    duty = 0
    while True:
        a2_pin.duty_u16(duty)
        reading = a1_pin.read()
        print(reading)

        duty = duty+10

        file.write(str(reading))
        file.write(', ')
        time.sleep(0.005)
        
        if reading >= 1000:
            over1000Counter+=1
        
        if reading >= 1023 and over1000Counter > 100:
            break


