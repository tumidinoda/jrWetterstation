from Temperatur import Temperatur
from KY-053_Sensor import KY-053_Sensor as KY053
import time
import RPi.GPIO as GPIO

sleepTime = 10

#temp = Temperatur()
ky053 = KY053()

try:
    while True:
        #temp.read()
        #temp.out()
        #temp.save()
        
		ky053.read()
		ky053.out()
		ky053.save()
		
		time.sleep(sleepTime)

except KeyboardInterrupt:
    GPIO.cleanup()
