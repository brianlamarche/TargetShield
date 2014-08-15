import time
import common

# 
# this says, hey we have a led strip
# with 32 LED's (pixels) 
# 
leds = common.LedPixel(32)

# please turn them all off
leds.allOff()

# this function pulses the colors
def pulse():
   colorfade(-1, -1, -1, False)
   colorfade(-1, -1, -1, True)

# this function fades all of the colors away
def colorfade(r, g, b, isback):
   red = r * 255
   green = g * 255
   blue = b * 255
   for c in range(255):
      if isback == True:
         c = 255 - c
      if r == -1:
         red = c
      if g == -1:
         green = c
      if b == -1:
         blue = c

      leds.allColor(red, green, blue)
      time.sleep(.001)

# this is the knight rider theme
def knight():
   t      = .0009
   bright = 180
   dimr = 1
   dimg = 1
   dimb = 1
   for i in range(-5, 26):
	for j in range(0, 32):
		leds.colorLed(j, dimr, dimg, dimb)
		leds.writeAll()
	for j in range(0, 5):
		delta = (j - 2) * bright
		if (i + j > 0 and i + j < 32):
			v = 255 - delta
			if (v < 0):
				v = 0
			elif (v > 255):
				v = 255
			leds.colorLed(i + j, v , 0, 0)
       		 	leds.writeAll()
	time.sleep(t)
   for i in range(26, -1, -1):
	for j in range(0, 32):
		leds.colorLed(j, dimr, dimg, dimb)
		leds.writeAll()
	for j in range(0, 5):
		delta = (j - 2) * bright
		if (i + j > 0 and i + j < 32):
			v = 255 - delta
			if (v < 0):
				v = 0
			elif (v > 255):
				v = 255
			leds.colorLed(i + j, v, 0, 0)
			leds.writeAll()

	time.sleep(t)

# this does a fade of all colors
def allcolors():
   leds.allOff()
   colorfade(-1, 0, 0, False)
   colorfade(1, -1, 0, False)
   colorfade(-1, 1, 0, True)
   colorfade(0, 1, -1, False)
   colorfade(0, -1, 1, True)
   colorfade(-1, 0, 1, False)
   colorfade(1, -1, 1, False)
   colorfade(-1, -1, -1, True)

# 
# this just says "hey do this forever"
# 
while True:
   pulse()
   allcolors()
   pulse()
