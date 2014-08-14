from targetIo 	import *
import time

#	
# This function shows you how to turn LED's on and off
# Does this look familiar?  It's the same code as 
# in the simple program.  But we put it in a function
# now we can just call this function instead of writing
# the code below over and over.
# It's a good way to keep your code concise and simple
# and allows you to reuse code anywhere in the program.
# 
def turnOnOff(t):
	# turn on one by one
	t.turnLedOn(0)
	time.sleep(1000)
	t.turnLedOn(1)
	time.sleep(1000)
	t.turnLedOn(2)
	time.sleep(1000)
	t.turnLedOn(3)
	time.sleep(1000)

	# turn off one by one
	t.turnLedOff(3)
	time.sleep(1000)
	t.turnLedOff(2)
	time.sleep(1000)
	t.turnLedOff(1)
	time.sleep(1000)
	t.turnLedOff(0)
	time.sleep(1000)

#
# this function shows you how to check for buttons
# a function takes parameters (things you pass into it)
# 
def checkButtons(t, loopCount):
	t.turnAllLedOn()

	# here we have a loop, that means, repeat the below
	# until i = loopCount.  i will increment by 1 every 
	# time the loop finishes executing its body
	for i in range(0, loopCount):
		# here we check all buttons - notice
		# we have another loop inside a loop?
		# We call this a nested loop (because the loop below
		# is nested within the loop above
		# range is actually a function that specifies 
		# a list of numbers between 0, and 3
		# each time the loop iterates
		# the button will increment by 1.  
		for button in range(0, 3):
			pressed = t.checkForButtonPress(button)
			if (pressed == True):
				t.turnLedOff(button)
		time.sleep(.001)

# does this look familiar?
t = TargetIo()
turnOnOff(t)
checkButtons(t, 1000)

#
# Challenge question:
#  how can you make the button checking last longer?
#