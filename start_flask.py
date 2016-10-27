from flask import Flask
from flask import request
from twilio import twiml
app = Flask(__name__)

@app.route("/")
def hello():
	print "They found us!"
	return "Hello, Aliens!"

@app.route('/add', methods=['GET'])
def addGet():
	return "Ah, ah, you didn't say the magic word..."

@app.route('/add', methods=['POST'])
def add():
	try:
		print request.form['Body']
		return "Message added"
	except Exception as e:
		print(e)

if __name__ == "__main__":
	app.run()

