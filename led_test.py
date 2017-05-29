from gpiozero import LED
import sys
import time
state=1

red=''
red=LED(23)

while True:
	red.on()
	time.sleep(1)
	red.off()
	time.sleep(1)
