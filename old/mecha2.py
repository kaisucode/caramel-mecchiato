
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)



GPIO.setwarnings(False)

PIN = 25
GPIO.setup(PIN, GPIO.OUT)
servo1 = GPIO.PWM(PIN, 50)
servo1.start(0)


angle = 20
duty = angle / 18 + 3


servo1.ChangeDutyCycle(duty)
time.sleep(1)
GPIO.output(PIN, False)
servo1.ChangeDutyCycle(0)



