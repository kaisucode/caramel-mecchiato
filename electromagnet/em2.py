
from gpiozero import Servo
from time import sleep

import RPi.GPIO as GPIO

#servo = Servo

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

ledpin = 18

GPIO.setup(ledpin, GPIO.OUT)

pwm = GPIO.PWM(ledpin, 1000)
pwm.start(0)


def high_test(): 
    GPIO.output(ledpin, GPIO.HIGH)
    print("high")
    sleep(5)
    GPIO.output(ledpin, GPIO.LOW)
    print("low")


def loop(): 
    while True: 
        for duty in range(0, 101, 10): 
            pwm.ChangeDutyCycle(duty)
            sleep(0.01)
            print("current duty: ", duty)
        sleep(10)

loop()
