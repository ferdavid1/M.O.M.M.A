from gpiozero import LED
import sys
import time
state=1

red=''
red=LED(23)

if state:
	red.on()
	time.sleep(.5)
	red.off()

else:
	red.off()
