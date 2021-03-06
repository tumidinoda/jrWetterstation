from KY052_Sensor import KY052_Sensor
from jrMail import JrMail

# ===============================================================================
# define cyclic logging
import logging.handlers
import traceback

LOG_FILENAME = '/home/robert/jrWetterstation/logs/jrWetterstation.log'

# Set up a specific logger with our desired output level
myLogger = logging.getLogger('jrWetterstationLogger')
# myLogger.setLevel(logging.DEBUG)
myLogger.setLevel(logging.INFO)
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=100000, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s-%(module)s-%(lineno)s-%(levelname)s-%(message)s', '%y%m%d-%H%M%S'))
myLogger.addHandler(handler)

# ===============================================================================
ky052 = KY052_Sensor()  # KY052 Sensor instance created
try:
    myLogger.debug('Wetterstation gestartet')
    ky052.read()
    ky052.save()

except Exception:
    errMsg = "Global exception handler: \n"
    errMsg += traceback.format_exc()
    myLogger.error(errMsg)
    myMail = JrMail()
    myMail.sendMail('Wetterstation: Global Exception', errMsg)
    pass

except:
    message = 'Global exception handler:\nProgram stopped by external interrupt'
    myLogger.error(message)
    print(message)
