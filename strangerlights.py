#!/usr/bin/python

# Stranger Things Christmas Lights
# Author: Paul Larson (djhazee@gmail.com)
#
# -Port of the Arduino NeoPixel library strandtest example (Adafruit).
# -Uses the WS2811 to animate RGB light strings (I am using a 5V, 50x RGB LED strand)
# -This will blink a designated light for each letter of the alphabet


# Import libs used
import emojis
import magic8Ball
import sys
import time
import random
import unicodedata
import ledFunctions

from ledSettings import *
from neopixel import *

#Start up random seed
random.seed()


# Other vars
ALPHABET = '****z*y**x*w**v***u**t***s**r*********i***j**k**l*m**n***o**p**q********h****g**f****e****d*c***b**a'  #alphabet that will be used
LIGHTSHIFT = 0  #shift the lights down the strand to the other end 
FLICKERLOOP = 3  #number of loops to flicker

def initLights(strip):
  """
  initializes the light strand colors 

  inputs: 
    strip = color strip instance to action against

  outputs:
    <none>
  """
  colorLen = len(COLORS)
  #Initialize all LEDs
  for i in range(len(ALPHABET)):
    strip.setPixelColor(i+LIGHTSHIFT, COLORS[i%colorLen])
  strip.show()

def getRandomNamedColor():
  """
  returns a random Color object
  inputs:
    <none>
  outputs:
    Color()
  """
  index = random.randint(0, len(NAMED_COLORS)-1)
  return NAMED_COLORS[index]

def randomDisplay(strip):
  routines = [runBlink,
    runDance,
    runItsHere]

  randomFunction = random.choice(routines)
  randomFunction(strip)

def randomColorWipe(strip):
  ledFunctions.colorWipe(getRandomNamedColor())
                           

def crazyBlinking(strip):
  """
  Blink the lights like crazy.
  """
  #now frantically blink all lights 
  for loop in range(7):
    #initialize all the lights
    initLights(strip)

    time.sleep(random.randint(50,150)/1000.0)

    #kill all lights
    for led in range(len(ALPHABET)):
      strip.setPixelColor(led+LIGHTSHIFT, OFF)
    strip.show()

    time.sleep(random.randint(50,150)/1000.0)

def blinkWords(strip, word, wait_ms=1000):
  """
  blinks a string of letters

  inputs: 
    strip = color strip instance to action against
    word = word to blink

  outputs:
    <none>
  """

  # Delay before showing message
  time.sleep(wait_ms/1000.0)
  
  word = word.lower()
  if word == 'where are you' or word == 'where are you?':
    word = '' # Prevent the question from displaying
    blinkWords(strip, 'right here')
  if word[len(word)-1] == '?':
    word = '' # Prevent the question from displaying
    magic8BallUsed = True
    blinkWords(strip, random.choice(magic8Ball.answers))
  else:
    for character in word.lower():
      charName = unicodedata.name(character)
      print(charName)
      if character in ALPHABET:
        strip.setPixelColor(ALPHABET.index(character)+LIGHTSHIFT, getRandomNamedColor())
        strip.show()
        time.sleep(1)
        strip.setPixelColor(ALPHABET.index(character)+LIGHTSHIFT, OFF)
        strip.show()
        time.sleep(.25)
      if charName in emojis.EMOJIS:
        print("Supported Emoji")
        emojis.runEmojiSequence(strip, charName)
      else:
        time.sleep(.75)

def flicker(strip, ledNo):
  """
  creates a flickering effect on a bulb

  inputs: 
    strip = color strip instance to action against
    ledNo = LED position on strand, as integer.

  outputs:
    <none>
  """
  #get origin LED color
  origColor = strip.getPixelColor(ledNo)

  #do FLICKERLOOP-1 loops of flickering  
  for i in range(0,FLICKERLOOP-1):

    #get current LED color, break out to individuals
    currColor = strip.getPixelColor(ledNo)
    currRed = (currColor & REDMASK) >> 16
    currGreen = (currColor & GREENMASK) >> 8
    currBlue = (currColor & BLUEMASK)

    #turn off for a random short period of time
    strip.setPixelColor(ledNo, OFF)
    strip.show()
    time.sleep(random.randint(10,50)/1000.0)

    #turn back on at random scaled color brightness
    #modifier = random.randint(30,120)/100
    modifier = 1
    #TODO: fix modifier so each RGB value is scaled. 
    #      Doesn't work that well so modifier is set to 1. 
    newBlue = int(currBlue * modifier)
    if newBlue > 255:
      newBlue = 255
    newRed = int(currRed * modifier)
    if newRed > 255:
      newRed = 255
    newGreen = int(currGreen * modifier) 
    if newGreen > 255:
      newGreen = 255
    strip.setPixelColor(ledNo, Color(newRed,newGreen,newBlue))
    strip.show()
    #leave on for random short period of time
    time.sleep(random.randint(10,80)/1000.0)

  #restore original LED color
  strip.setPixelColor(ledNo, origColor)

def runDance(strip):
  runBlink(strip, "dance")

def runItsHere(strip):
  runBlink(strip, "its here")

def runBlink(strip, word='run'):
  """
  blinks the RUN letters

  inputs: 
    strip = color strip instance to action against

  outputs:
    <none>
  """
  #first blink the word "run", one letter at a time
  blinkWords(strip, word)

  #now frantically blink all 3 letters
  for loop in range(20):
    #turn on all three letters at the same time
    for character in word:
      if character in ALPHABET:
        strip.setPixelColor(ALPHABET.index(character)+LIGHTSHIFT, RED)
    strip.show()

    time.sleep(random.randint(15,100)/1000.0)

    #turn off all three letters at the same time
    for character in word:
      if character in ALPHABET:
        strip.setPixelColor(ALPHABET.index(character)+LIGHTSHIFT, OFF)
    strip.show()

    time.sleep(random.randint(50,150)/1000.0)

  #now frantically blink all lights 
  for loop in range(15):
    #initialize all the lights
    initLights(strip)

    time.sleep(random.randint(50,150)/1000.0)

    #kill all lights
    for led in range(len(ALPHABET)):
      strip.setPixelColor(led+LIGHTSHIFT, OFF)
    strip.show()

    time.sleep(random.randint(50,150)/1000.0)

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
  strip.begin()

  print ('Press Ctrl-C to quit.')


  while True:

    ##Initialize all LEDs
    for i in range(len(ALPHABET)):
      strip.setPixelColor(i+LIGHTSHIFT, Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
      strip.show()

    #initialize all the lights
    initLights(strip)
    
    time.sleep(random.randint(5,15))

    #flicker each light, no delay between each
    for i in range(20):
      flicker(strip,random.randint(LIGHTSHIFT,len(ALPHABET)+LIGHTSHIFT))
      time.sleep(random.randint(10,50)/1000.0)

    time.sleep(2)

    #flash lights to word
    word = 'its here'
    blinkWords(strip, word)
    runBlink(strip)
    time.sleep(1)

    #create a list of jumbled ints
    s = list(range(len(ALPHABET)))
    random.shuffle(s)

    #turn on each light in a semi-random fasion
    colorLen = len(COLORS)
    #Initialize all LEDs
    for i in range(len(ALPHABET)):
      strip.setPixelColor(s[i]+LIGHTSHIFT, COLORS[s[i]%colorLen])
      strip.show()
      time.sleep(random.randint(10,80)/1000.0)
