import auth
from twilio.rest import TwilioRestClient

client = TwilioRestClient(auth.account_sid, auth.auth_token)

message = client.messages.create(body="The spirits are thinking of you...",
	to="+19192717655",
	from_=auth.twilio_number)

print(message.sid) 
