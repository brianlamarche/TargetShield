import time
import common

# 
# this says, hey we have a led strip
# with 32 LED's (pixels) 
# 
leds = common.LedPixel(32)

# please turn them all off
leds.allOff()

# then simply color things
# colors range from 0 to 255 (the size of a byte)
leds.colorLed(0, 255, 	0,   0)		# first 	is red
leds.colorLed(1, 0,      255,   0)		# second 	is green
leds.colorLed(2, 0, 	 	0,   255)		# third 	is blue
leds.writeAll()
time.sleep(1)

# colors range from 0 to 255 (the size of a byte)
leds.colorLed(0, 0, 	 	0,   255)		# first 	is blue
leds.colorLed(1, 255, 	0,   0)		# second 	is red
leds.colorLed(2, 0,      255,   0)		# third 	is green
leds.writeAll()
time.sleep(1)

# colors range from 0 to 255 (the size of a byte)
leds.colorLed(0, 0,      255,   0)		# first 	is green
leds.colorLed(1, 0, 	 	0,   255)		# second 	is blue
leds.colorLed(2, 255, 	0,   0)		# thid 	is red
leds.writeAll()
time.sleep(1)

# colors range from 0 to 255 (the size of a byte)
leds.colorLed(0, 255, 	0,   0)		# first 	is red
leds.colorLed(1, 0,      255,   0)		# second 	is green
leds.colorLed(2, 0, 	 	0,   255)		# third 	is blue
leds.writeAll()
time.sleep(1)
