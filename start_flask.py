import pymongo
from auth import *
from urllib2 import urlopen
from flask import Flask
from flask import request
from twilio import twiml
app = Flask(__name__)

# Connect to the Monog database. This DB needs a single collection called 'messages'.
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
		# Save message to Monog database
		x = db.messages.insert({"unread": True, "body": request.form['Body']})
		print request.form['Body']
		print x

		# TODO: Format proper return twiml. The display will function without this
    # but you will see errors in the Twilio console.
		return "Message added"
	except Exception as e:
		print(e)

if __name__ == "__main__":
	app.run()
	
