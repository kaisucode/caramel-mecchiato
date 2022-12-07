
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit

import json
#  import requests
#  import os
#  import uuid

PORT = 5000
app = Flask(__name__)

cors = CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/voice_command', methods=["POST"])
def voice_command(): 
    action = request.json["message"]
    part = request.json["part"]
    print("action: ", action)
    print("part: ", part)

    #  socketio.emit('pi_do', { 'message': message })
    return jsonify({"status": "success"}), 200


#  @socketio.on('connect', namespace="/websockets")
#  def connect(): 
#      print("a user connected")

#  @socketio.on('disconnect')
#  def disconnect():
#      print(request.namespace.socket.sessid + " disconnected")

#  @socketio.on('send_message', namespace="/websockets")
#  def send_message(data): 
#      message = data["message"]
#      print("received and sending: " + message)
#      socketio.emit('pi_do', { 'message': message })


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=PORT, debug=True)



