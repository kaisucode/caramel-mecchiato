
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit

import json
import pi_servo_hat
import time


test = pi_servo_hat.PiServoHat()
test.restart()

PORT = 5000
app = Flask(__name__)

cors = CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config['CORS_HEADERS'] = 'Content-Type'


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
a_sword = Sword()

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

@app.route('/voice_command', methods=["POST"])
def voice_command(): 
    action = request.json["message"]
    part = request.json["part"]
    print("action: ", action)
    print("part: ", part)

	shutdown()

    if action == "initialize": 
        initialize()
    elif action == "calibrate": 
        calibrate()
    elif action == "diagostics": 
        run_diagnostics()
    elif action == "raise" or "lift": 
        test_high(part)
    elif action == "lower": 
        tesT_low(part)
    elif action == "sword": 
        a_sword.extend_sword()

	shutdown()

    #  socketio.emit('pi_do', { 'message': message })
    return jsonify({"status": "success"}), 200



def main():
	#circular_move_all(test_indices, move_range)
	#smooth_move(15, 70)
	#smooth_move(15, 70, reverse=True)

	initialize()


	calibrate()
	run_diagnostics()

	# sword demo
	#a_sword.extend_sword()

	shutdown()
	return


if __name__ == "__main__":
    socketio.run(app, host="169.254.96.19", port=PORT, debug=True)




