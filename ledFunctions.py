# NeoPixel library LED functions.
# Author: Scott Heath (gscottheath@gmail.com)
#
# Control NeoPixel animations.
# Based on Tony Dicola's direct port of the Arduino NeoPixel library strandtest example.

import ledSettings
import time

from neopixel import *

def allOn(strip, color=ledSettings.WHITE):
        """
        Sets all pixels to the provided color.
        """
        for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
        strip.show()

def allOff(strip):
        """
        Turns off all the LEDS.
        """
        for i in range(strip.numPixels()):
                strip.setPixelColor(i, ledSettings.OFF)
        strip.show()

def blinkNumTimes(strip, color=ledSettings.WHITE, numberOfBlinks=1, wait_ms=1000):
        """
        Blinks the strip for the specified number of times.
        Can specify the color and delay between blinks.
        """
        for num in range(0, numberOfBlinks):
                allOn(strip, color)
                time.sleep(wait_ms/1000.0)
                allOff(strip)
                time.sleep(wait_ms/1000.0)
        
def colorWipe(strip, color, wait_ms=50):
	"""
        Wipe color across display a pixel at a time.
        """
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)
