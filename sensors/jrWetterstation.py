import traceback

from jrPyCore.jrLogger import JrLogger
from jrPyCore.jrMail import JrMail
from sensors.sensor_KY052 import SensorKY052

# -----------------------------------------------------------------------------------------------------
logger = JrLogger().config(__name__)
try:

    logger.info('Wetterstation gestartet')
    ky052 = SensorKY052()
    ky052.read()
    ky052.save()

except Exception:
    err_msg = "Global exception handler: \n"
    err_msg += traceback.format_exc()
    logger.exception(err_msg)
    myMail = JrMail()
    myMail.send('Wetterstation: Global Exception', err_msg)
    pass

except:
    err_msg = 'Global exception handler:\nProgram stopped by external interrupt'
    logger.exception(err_msg)
