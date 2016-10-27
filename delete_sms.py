import sys
import auth
from twilio.rest import TwilioRestClient

client = TwilioRestClient(auth.account_sid, auth.auth_token)

def deleteMessage(message_id):
	print "Deleting message: " + message_id
	client.messages.delete(message_id)

print sys.argv

if sys.argv[1] == "-id":
	delete_id = sys.argv[2]
	if len(delete_id) == 34:
		deleteMessage(delete_id)
			
