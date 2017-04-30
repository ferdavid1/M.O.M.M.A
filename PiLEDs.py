from gpiozero import LED
import sys
state=sys.argv[1]
green=LED(14)
red=LED(2)
blue=LED(15)


if state:
	red.on()
else:
	red.off()
