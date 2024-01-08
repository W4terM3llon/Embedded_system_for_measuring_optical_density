from machine import Pin, ADC, PWM
import time
import constants as cnst

pow2_16 = 2**16-1
pow2_12 = 2**12-1

class Measurement:
    def __init__(self, duty, freq):
        self.duty = duty
        self.freq = freq
        
        self.a1_pin = ADC(25)
        self.a1_pin.atten(ADC.ATTN_11DB)
        self.a1_pin.width(ADC.WIDTH_12BIT)

        self.a2_pin = PWM(Pin(33), freq=self.freq, duty=self.duty)

    def measure(self):
        self.a2_pin.duty(self.duty)
        self.a2_pin.freq(self.freq)

        reading = self.a1_pin.read_uv()
        scaledReading = (reading - cnst.minDutyReadUv) / (cnst.maxDutyReadUv - cnst.minDutyReadUv)
        print(scaledReading)

        file.write(f"{scaledReading}, {self.duty}\n")
        time.sleep(0.0001)

freq = {1: 200_000, 2: 200_000, 3: 10_000, 4: 100_000, 5: 4_000_000}
for i in range(1, 2): # change which measurements are done
    measurement = Measurement(0, freq[i])
    with open(f'data{i}.txt','w') as file:
        for duty in range(1023):
            measurement.duty = duty
            measurement.measure()



