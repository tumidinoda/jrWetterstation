import traceback

from jrPyCore.jrLogger import JrLogger
from jrPyCore.jrMail import JrMail
from sensor_K052 import SensorKY052


# ---------------------------------------------------------------------------------------------------------
def main():
    my_logger = JrLogger().get()
    try:
        my_logger.info('Wetterstation gestartet')
        ky052 = SensorKY052()
        ky052.read()
        ky052.save()
    except:
        err_msg = "Global exception handler: \n"
        err_msg += traceback.format_exc()
        my_logger.exception(err_msg)
        my_mail = JrMail()
        my_mail.send('Wetterstation: Global Exception', err_msg)
        raise


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
