import auth
from twilio.rest import TwilioRestClient

client = TwilioRestClient(auth.account_sid, auth.auth_token)

def retriveMessages():
	for message in client.messages.list(to=auth.twilio_number):
		print message.sid + " " +  message.body

	
