from Temperatur import Temperatur
import time
import RPi.GPIO as GPIO

sleepTime = 10

temp = Temperatur()

try:
    while True:
        temp.read()
        #temp.out()
        temp.save()
        time.sleep(sleepTime)

except KeyboardInterrupt:
    GPIO.cleanup()
