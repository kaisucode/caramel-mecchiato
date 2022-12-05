

from gpiozero import Servo
from time import sleep

servo = Servo(25)

print("going to min")
servo.min()
sleep(2)
print("going to max")
servo.max()
sleep(2)
servo.mid()
