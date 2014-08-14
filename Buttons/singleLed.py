from targetIo 	import *
import time


# Can you figure out how to make the second LED turn on and off?
# Challenge - can you make it a variable????
t = TargetIo()
t.turnLedOn(0)
time.sleep(1)
t.turnLedOff(0)
