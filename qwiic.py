

import pi_servo_hat
import time

test = pi_servo_hat.PiServoHat()
test.restart()


OTHER = 2
shoulder = 4



def circular_move_all(test_indices, move_range): 
    for val in test_indices: 
        test.move_servo_position(val, 0)

    time.sleep(1)

    for val in test_indices: 
        test.move_servo_position(val, move_range)
    time.sleep(1)

    for val in test_indices: 
        test.move_servo_position(val, 0)
    time.sleep(1)


def test2(): 
    # Moves servo position to 0 degrees (1ms), Channel 0
    test.move_servo_position(0, 0)
    test.move_servo_position(shoulder, 0)
    test.move_servo_position(OTHER, 0)

    # Pause 1 sec
    time.sleep(1)

    # Moves servo position to 90 degrees (2ms), Channel 0
    test.move_servo_position(0, 90)
    test.move_servo_position(shoulder, 90)
    test.move_servo_position(OTHER, 90)

    # Pause 1 sec
    time.sleep(1)

#test_indices = [0, 2, 4]
test_indices = [0, 1, 15]
move_range = 35

def smooth_move(servo, end, start=0): 

	direction = 1 if (end >= start) else -1
	start, end, order = start, end, direction

	for i in range(start, end, order): 
		test.move_servo_position(servo, i)
		time.sleep(0.005)


def rotation_test(servo, smooth=True): 

	#test.move_servo_position(servo, 0)
	smooth_move(servo, 0)
	print("moved to 0")
	time.sleep(1)

	#test.move_servo_position(servo, 90)
	smooth_move(servo, 90)
	print("moved to 90")
	time.sleep(1)

	#test.move_servo_position(servo, 0)
	smooth_move(servo, 90, True)
	print("moved to 0")
	time.sleep(1)


def initialize(): 
	print("Initializing...")
	for i in range(0, 16): 
		test.move_servo_position(0, 0)
	print("Initialized")


class Sword: 
	def __init__(self, servo_pin=3): 
		self.servo = servo_pin

	def stop_sword(self): 
			test.move_servo_position(self.servo, 0)
			print("sword stopped")

	def extend_sword(self, reverse=False):

		self.stop_sword()
		if reverse: 
			test.move_servo_position(self.servo, 0)
			print("sword retracted")
		else: 
			test.move_servo_position(self.servo, 158)
			print("sword extended")

		time.sleep(1.5)
		self.stop_sword()

def shutdown(): 
	test.restart()


def left_shoulder_demo(): 
	print("begin left shoulder demo")
	smooth_move(15, start=0, end=50)

	time.sleep(2)

	smooth_move(15, start=30, end=0)
	#rotation_test(15)
	#test.move_servo_position(3, 0)
	#smooth_move(3, 0)


def run_tests(): 


	left_shoulder_demo()

	# sword demo
	#a_sword.extend_sword()
	#time.sleep(1)
	#a_sword.extend_sword(reverse=True)



	


def main():
	#circular_move_all(test_indices, move_range)
	#smooth_move(15, 70)
	#smooth_move(15, 70, reverse=True)

	#initialize()

	run_tests()
	a_sword = Sword()

	shutdown()
	return

	smooth_move(0, 0)
	smooth_move(0, 45)
	smooth_move(0, 0)
	print("moved to 0")
	#smooth_move(15, 70, reverse=True)


if __name__ == "__main__":
	main()





