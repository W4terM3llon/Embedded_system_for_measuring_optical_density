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

def sth():
    measurement = Measurement(DUTY, FREQ)
    with open(f'data{i}.txt','w') as file:
        for duty in range(1023):
            measurement.duty = duty
            measurement.measure()
