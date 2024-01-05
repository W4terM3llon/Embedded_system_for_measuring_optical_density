from machine import Pin, ADC
import time

A0_NO = 26
A1_NO = 25
a0_pin = Pin(A0_NO, Pin.OUT)
a1_pin = ADC(A1_NO)
a1_pin.atten(ADC.ATTN_11DB)
a1_pin.width(ADC.WIDTH_10BIT)
while True:
    a0_pin.value(1 if a0_pin.value() == 0 else 0)
    print(a1_pin.read())
    time.sleep(0.5)

    