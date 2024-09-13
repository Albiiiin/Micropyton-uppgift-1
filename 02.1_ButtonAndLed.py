from machine import Pin
import time

led = Pin(15, Pin.OUT)                   
button = Pin(13, Pin.IN, Pin.PULL_UP)    #Create button object from Pin13 , Set GP13 to input

def send_sos(num_of_sos):
    for _ in range(num_of_sos):
        for _ in range(3)
            led.value(1)
            time.sleep(0.2)
            led.value(0)
            time.sleep(0.2)

        for _ in range(3)
            led.value(1)
            time.sleep(0.6)
            led.value(0)
            time.sleep(0.2)

        for _ in range(3)
            led.value(1)
            time.sleep(0.2)
            led.value(0)
            time.sleep(0.2)
        
        time.sleep(1)
        

try:
    while True:
        if not button.value():
            send_sos(2)                #Set led turn on
            while not button.value():
                pass
        else:
            led.value(0)                #Set led turn off
except:
    pass