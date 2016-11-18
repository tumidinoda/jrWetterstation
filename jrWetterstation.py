from Temperatur import Temperatur
from KY053_Sensor import KY053_Sensor as KY053
import time
import RPi.GPIO as GPIO

#===============================================================================
#define cyclic logging
import glob
import logging
import logging.handlers

LOG_FILENAME = 'jrWetterstation-Log'

# Set up a specific logger with our desired output level
myLogger = logging.getLogger('jrWetterstationLogger')
myLogger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=100000, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s-%(module)s-%(lineno)s-%(levelname)s-%(message)s','%y%m%d-%H%M%S'))
myLogger.addHandler(handler)


#===============================================================================
#define global variables
sleepTime = 10
#temp = Temperatur()
ky053 = KY053()   #KY053 Sensor instance created
#===============================================================================
try:
    while True:
        #temp.read()
        #temp.out()
        #temp.save()
        
        ky053.read()
#       ky053.out()
        ky053.save()
        
        time.sleep(sleepTime)

except KeyboardInterrupt:
    myLogger.debug('Program stopped by keyboard interupt')
    GPIO.cleanup()
