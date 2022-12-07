

import pi_servo_hat
import time

test = pi_servo_hat.PiServoHat()
test.restart()


OTHER = 2
shoulder = 4

settings = {
	"mk6": {
		"starting_pos": {15: 120, 14: 45, 0: 160}, # servo_pin, degrees
		"ending_pos": {15: 30, 14: 0, 0: 100}, # servo_pin, degrees
		"pins": {
			"left_shoulder": 15,
			"left_arm": 14,
			"right_chest": 0,
			"right_shoulder": 1,
			"right_arm": 2,
			"sword": 3,
		}, 
	}
}

cur_mode = "mk6"

def get_pin(name): 
	return settings[cur_mode]["pins"][name]

def get_starting_pos(name): 
	pin = get_pin(name)
	return settings[cur_mode]["starting_pos"].get(pin, 0)
def get_ending_pos(name): 
	pin = get_pin(name)
	return settings[cur_mode]["ending_pos"].get(pin, 30)

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


def smooth_move(servo, end, start=0): 

	direction = 1 if (end >= start) else -1
	start, end, order = start, end, direction

	for i in range(start, end, order): 
		test.move_servo_position(servo, i)
		time.sleep(0.006)


def initialize(): 
	print("Initializing...")
	time.sleep(1)
	for i in range(0, 16): 
		position = settings[cur_mode]["starting_pos"].get(i, 0)
		test.move_servo_position(i, position)
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


def test_limits_circular(name): 
	pin = get_pin(name)
	starting_pos = get_starting_pos(name)
	ending_pos = get_ending_pos(name)

	smooth_move(pin, start=starting_pos, end=ending_pos)
	time.sleep(0.5)
	smooth_move(pin, start=ending_pos, end=starting_pos)


def test_high(name): 
	pin = get_pin(name)
	starting_pos = get_starting_pos(name)
	ending_pos = get_ending_pos(name)
	#smooth_move(pin, start=starting_pos, end=ending_pos)
	test.move_servo_position(pin, ending_pos)

def test_low(name): 
	pin = get_pin(name)
	starting_pos = get_starting_pos(name)
	ending_pos = get_ending_pos(name)
	#smooth_move(pin, start=ending_pos, end=starting_pos)
	test.move_servo_position(pin, starting_pos)

def calibrate(): 

	# individual movement
	#for part in ["right_chest"]: 
	for part in ["left_shoulder", "left_arm", "right_chest"]: 
		print("begin " + part + " demo")
		test_limits_circular(part)
		time.sleep(0.3)

def run_diagnostics(): 

	for i in ["left_shoulder", "left_arm", "right_chest"]: 
		test_high(i)
	time.sleep(1)
	for i in ["left_shoulder", "left_arm", "right_chest"]: 
		test_low(i)



def main():
	#circular_move_all(test_indices, move_range)
	#smooth_move(15, 70)
	#smooth_move(15, 70, reverse=True)

	initialize()

	a_sword = Sword()

	calibrate()
	run_diagnostics()

	# sword demo
	#a_sword.extend_sword()

	shutdown()
	return


if __name__ == "__main__":
	main()





