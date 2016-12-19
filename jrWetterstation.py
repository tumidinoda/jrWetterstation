from Temperatur import Temperatur
from KY052_Sensor import KY052_Sensor as KY052
import time
import RPi.GPIO as GPIO

#===============================================================================
#define cyclic logging
import glob
import logging
import logging.handlers

LOG_FILENAME = 'jrWetterstation-Log.log'

# Set up a specific logger with our desired output level
myLogger = logging.getLogger('jrWetterstationLogger.log')
#myLogger.setLevel(logging.DEBUG)
myLogger.setLevel(logging.INFO)
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=100000, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s-%(module)s-%(lineno)s-%(levelname)s-%(message)s','%y%m%d-%H%M%S'))
myLogger.addHandler(handler)


#===============================================================================
#define global variables
sleepTime = 5
#temp = Temperatur()
ky052 = KY052()   #KY052 Sensor instance created
#===============================================================================
try:
    myLogger.info('\n\nWetterstation gestartet\n')
    while True:
        #temp.read()
        #temp.out()
        #temp.save()
        
        ky052.read()
#       ky052.out()
        ky052.save()
        
        time.sleep(sleepTime)

except Exception:
    myLogger.error('Global: unhandled exception. Continue program')
    pass

except:
    message='Global: Program stopped by external interrupt'
    myLogger.error(message)
    print message
    GPIO.cleanup()
