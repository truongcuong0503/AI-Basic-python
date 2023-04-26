import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

with speech_recognition.Microphone() as mic:
	print("Robot: I'm Listening")
	audio = robot_ear.listen(mic)
	print("Robot: ....")

try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""

	print("You: " + you)

if you == "":
	robot_brain = "I can hear you, try again"
elif "Hello" in you:
	robot_brain = "Hello"
elif "today" in you:
	today = date.today()
	robot_brain = today.strftime("%B %d, %Y")
elif "time" in you:
	now = datetime.now()
	robot_brain = now.strftime("%H hours %M munites %S seconds")
elif "president" in you:
	robot_brain = "Donald Trump"
elif "bye" in you:
	robot_brain = "Bye"
	print("robot_brain: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
		

	print("robot_brain: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()