

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

def smooth_move(servo, angle, reverse=False): 

    start, end, order = 0, angle, 1
    if reverse: 
        start, end, order = angle, 0, -1

    for i in range(start, end, order): 
        test.move_servo_position(servo, i)
        time.sleep(0.005)


def rotation_test(servo): 

	test.move_servo_position(servo, 0)
	print("moved to 0")
	time.sleep(1)

	test.move_servo_position(servo, 90)
	print("moved to 90")
	time.sleep(1)

	test.move_servo_position(servo, 0)
	print("moved to 0")
	time.sleep(1)


def initialize(): 
	for i in range(0, 16): 
		test.move_servo_position(0, 0)


def stop_sword(servo=3): 
		test.move_servo_position(servo, 0)
		print("sword stopped")

def extend_sword(servo=3, reverse=False):

	if reverse: 
		test.move_servo_position(servo, 0)
		print("sword retracted")
	else: 
		test.move_servo_position(servo, 158)
		print("sword extended")
	

def main():
	#circular_move_all(test_indices, move_range)
	#smooth_move(15, 70)
	#smooth_move(15, 70, reverse=True)

	initialize()
	print("initialized")

	extend_sword()
	time.sleep(1)
	extend_sword(reverse=True)


	#rotation_test(3)
	#test.move_servo_position(3, 0)
	#smooth_move(3, 0)
	return

	smooth_move(0, 0)
	smooth_move(0, 45)
	smooth_move(0, 0)
	print("moved to 0")
	#smooth_move(15, 70, reverse=True)


if __name__ == "__main__":
	main()





