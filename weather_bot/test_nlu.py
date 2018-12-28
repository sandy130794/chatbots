from rasa_nlu.model import Interpreter
import json

def run_nlu():
	interpreter = Interpreter.load("./models/nlu/weather/weather_report")
	message = "I planning my holiday to Jammu and Kashmir. I want to know the weather out there."
	result = interpreter.parse(message)
	print(json.dumps(result, indent=2))

if __name__ == '__main__':
	run_nlu()