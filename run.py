import pymongo
import ledFunctions
from ledSettings import *
from neopixel import *
from strangerlights import *

# Connect to Mongo database
client = pymongo.MongoClient("localhost", 27017)
db = client.local

def getNextMessage():
  """
  Fetch the next unread message from the queue.
  """
  msg = db.messages.find_one({'unread': True})
  if msg:
    db.messages.update({'_id': msg['_id']}, {'$set': {'unread': False}})
    return msg['body']

# Main program logic follows:
if __name__ == '__main__':
  print ('Press Ctrl-C to quit.')

  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
  strip.begin()

  timeout = 15
  count = timeout
  while True:
    nextMsg = getNextMessage()
    if nextMsg:
      # Frantically blink the lights then play the message
      count = timeout
      crazyBlinking(strip)
      blinkWords(strip, nextMsg)
    if count <= 0:
      # If no new message has been received and the loop times out,
      # then play a random display
      randomDisplay(strip)
      count = 5

    time.sleep(1)
    # Decrement the count for the timeout
    if count > 0:
      count -= 1
  
  
