
#git clone https://github.com/Majdawad88/ECET411_LED_Ex1.git

import RPi.GPIO as GPIO
import time

LED = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping...")
finally:
    GPIO.cleanup()  # MUST run to prevent lgpio 'GPIO busy' errors
