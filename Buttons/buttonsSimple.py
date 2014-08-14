# This tells Python "Hey we have other code in another file
# we want you to use, so import it so we can use it here
# 
from targetIo 	import *
import time

# we need this 'object' so we can talk to the board
# to tell it what actions to take (e.g. Turn on an LED)
# notice the first LED and Button all start with 0
# and we act like they are in a list (array)
# so 
#	button 1 is position or index 0
#	button 2 is position or index 1
#	button 3 is position or index 2
#	button 4 is position or index 3
# all (most) of computer science counts for arrays start at 0
# 
t = TargetIo()
	
# turn LED's on one by one - here we turn on the first LED
t.turnLedOn(0)

# then wait some time 
#     SO ...in seconds, so .1 seconds = 100 millisecond
time.sleep(1)	
t.turnLedOn(1)
time.sleep(1)
t.turnLedOn(2)
time.sleep(1)
t.turnLedOn(3)
time.sleep(1)

# then we turn off one by one
t.turnLedOff(3)
time.sleep(1)
t.turnLedOff(2)
time.sleep(1)
t.turnLedOff(1)
time.sleep(1)
t.turnLedOff(0)
time.sleep(1)

# this function in t says "Hey turn them all back on again."
t.turnAllLedOn()
time.sleep(1)

# then herewe are checking to see if the first button (0th 
# position) is pressed. What would happen if we 
# typed 1 instead of 0 below?

#check the first button, you must press and hold button one
pressed = t.checkForButtonPress(0)

# here we write a message to the screen by typing 
# print "message" - print is a way to display text
# on the screen and is useful for debugging
print "The button was pressed: ", pressed
if (pressed == True):
	t.turnLedOff(0)

#
# Challenge Question?
# Why must the button be held before t.CheckForButtonPress(0)
# is called???
# 
