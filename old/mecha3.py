

from gpiozero import Servo
from time import sleep

servo = Servo(25)

try: 
    while True: 
        servo.min()
        print("going to min")
        sleep(0.5)
        #servo.mid()
        #print("going to mid")
        #sleep(0.5)
        #servo.max()
        #print("going to max")
        #sleep(0.5)
except KeyboardInterrupt: 
    print("stopped")
