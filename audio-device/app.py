
import speech_recognition as sr
import os
import requests
import socketio

#  URL = "http://0.0.0.0:5000/"
URL = "http://0.0.0.0:5000/"
sio = socketio.Client()
sio.connect(URL)

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def disconnect():
    print("I'm disconnected!")


def sayCommand(newCommand): 
    print(newCommand)
    tts = gTTS(text=newCommand, lang='en-uk', slow='true')
    tts.save("data/command1.mp3")
    os.system("mpg123 -d 2 data/command1.mp3 &")


def parse_command(command): 
    split_text = command.split(" ")
    processedCommand = command.lower()
    print("processedCommand: " + processedCommand)

    action = split_text[0]
    part = "_".join(split_text[1:])

    if action == "raised":
        action = "raise"

    valid_actions = ["raise", "lower", "initialize", "calibrate"]
    if action not in valid_actions: 
        print("command not found")
        return

    res = requests.post(URL + "voice_command", json={'message': action, 'part': part })
    print("sent message {command} to server".format(command=processedCommand))

while(1): 
    print("\n\n---\nwaiting for new command")
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        print("received audio clip, processing...")

        command = r.recognize_google(audio)
        print("Original command: " + command)
        parse_command(command)

    except Exception as e:
        print(e)


