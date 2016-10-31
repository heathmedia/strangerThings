import pymongo
from auth import *
from urllib2 import urlopen
from flask import Flask
from flask import request
from twilio import twiml
app = Flask(__name__)

client = pymongo.MongoClient("localhost", 27017)
db = client.local

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
		# Save message to Firebase dastabase
		x = db.messages.insert({"unread": True, "body": request.form['Body']})
		print request.form['Body']
		print x

		# TODO: Format proper return twiml
		return "Message added"
	except Exception as e:
		print(e)

if __name__ == "__main__":
	app.run()
	
