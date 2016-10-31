# Emoji selector for Neopixels
# Author: Scott Heath (gscottheath@gmail.com)
#
# Control NeoPixel animations.
# Based on Tony Dicola's direct port of the Arduino NeoPixel library strandtest example.

import ledFunctions
import ledSettings
import random
import time

EMOJIS = [
  'JACK-O-LANTERN',
  'PILE OF POO',
  'GHOST',
  'SNAKE',
  'DRAGON',
  'DRAGON FACE',
  'SMILING FACE WITH HEART-SHAPED EYES',
  'SMILIN CAT FACE WITH HEART-SHAPED EYES',
  'FACE THROWING A KISS',
  'HEAVY BLACK HEART',
  'RAINBOW',
  'REGIONAL INDICATOR SYMBOL LETTER U']

def jackOLantern(strip):
    for loop in range(0,3):
        # Set all leds to Orange except for the Green stem
        for pixel in range(strip.numPixels()):
            color = ledSettings.ORANGE
            if pixel in range(82, 86):
                color = ledSettings.GREEN
            strip.setPixelColor(pixel, color)
        strip.show()
        # Wait 5s on the last loop, otherwise wait 1s
        if loop == 2:
            time.sleep(5)
        else:
            time.sleep(1)
        ledFunctions.allOff(strip)
        time.sleep(1)

def pileOfPoo(strip):
    ledFunctions.blinkNumTimes(strip, ledSettings.BROWN, 3)

def rainbow(strip):
    option = random.randint(1,3)
    #if option == 1:
        #ledFunctions.rainbowCycle(strip)
    if option == 2:
        ledFunctions.theaterChaseRainbow(strip)
    else:
        ledFunctions.rainbow(strip)

def snake(strip):
    ledFunctions.colorWipe(strip, ledSettings.GREEN)

def hearts(strip):
    ledFunctions.colorWipe(strip, ledSettings.RED)

def ghost(strip, ghostLength=3, wait_ms=50):
    """
    A ghostly apparition that travels along the LED strip.
    Set ghostLength to make your ghost bigger or smaller.
    Set wait_ms to make your ghost faster or slower.
    """
    
    for i in range(strip.numPixels()):
            strip.setPixelColor(i, ledSettings.WHITE)
            if i >= ghostLength:
                strip.setPixelColor(i - ghostLength, ledSettings.OFF)
            strip.show()
            time.sleep(wait_ms/1000.0)

def usa(strip, wait_ms=1000):
    """
    Blink the ole RED, WHITE, & BLUE.
    """
    ledFunctions.allOn(strip, ledSettings.RED)
    time.sleep(wait_ms/1000.0)
    ledFunctions.allOn(strip, ledSettings.WHITE)
    time.sleep(wait_ms/1000.0)
    ledFunctions.allOn(strip, ledSettings.BLUE)
    time.sleep(wait_ms/1000.0)
    ledFunctions.allOn(strip, ledSettings.OFF)

def randomSequence(strip):
    randomEmoji = random.choice(EMOJIS)
    runEmojiSequence(strip, randomEmoji)

def runEmojiSequence(strip, charName):
    """
    Selects an emoji sequence to run based of the emoji's unicode description
    """
    
    ledFunctions.allOff(strip)

    # Select a supported emjoy sequence
    if charName == 'JACK-O-LANTERN':
        jackOLantern(strip)
    if charName == 'PILE OF POO':
        pileOfPoo(strip)
    if charName == 'RAINBOW':
        rainbow(strip)
    if charName == 'SNAKE' or charName == 'DRAGON' or charName == 'DRAGON_FACE':
        snake(strip)
    if charName == 'SMILING FACE WITH HEART-SHAPED EYES' or charName == 'FACE THROWING A KISS' or charName == 'SMILIN CAT FACE WITH HEART-SHAPED EYESHEART':
        hearts(strip)
    if charName == 'GHOST':
        ghost(strip)
    if charName == 'REGIONAL INDICATOR SYMBOL LETTER U':
        usa(strip)

    ledFunctions.allOff(strip)
