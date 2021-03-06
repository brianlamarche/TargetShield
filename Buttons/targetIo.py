import  RPi.GPIO as GPIO

SENSOR_HIT 	= False
LED_ON 		= True

#
# this is an class - object - that has 
# functions in them.
# 
# This is a more advanced subject but shows you
# how you can use Python in an object oriented way
#
class TargetIo:
	def __init__(self):
		self.pins = [11, 15, 16, 22]
		self.leds = {0:11,
				  1:15,
				  2:16,
				  3:22
			       }
		self.buttons = {0:7,
				     1:13,
				     2:12,
				     3:18
			          }				
		self.configure()

	def configure(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		for i in range(0, 4):
			led    = self.leds[i]
			button = self.buttons[i]
			GPIO.setup(button, GPIO.IN)
			GPIO.setup(led,    GPIO.OUT)

	def turnLedOn(self, led):
		pin 	 = self.leds[led]
		GPIO.output(pin, True)
			
	def turnLedOff(self, led):
		pin 	 = self.leds[led]
		GPIO.output(pin, False)

	def turnAllLedOff(self):
		#GPIO.setwarnings(False)
		#GPIO.setmode(GPIO.BOARD)
		for pin in self.pins:
			GPIO.setup(pin,   GPIO.OUT)			
			GPIO.output(pin, False)

	def turnAllLedOn(self):
		for pin in self.pins:
			GPIO.setup(pin,   GPIO.OUT)			
			GPIO.output(pin, True)

	def checkForButtonPress(self, button):
		for pin in self.pins:
			pin    = self.buttons[button]
			isHigh = GPIO.input(pin)
			if (isHigh == SENSOR_HIT):
				return True
		return False





