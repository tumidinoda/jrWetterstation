import logging
import rrdtool
from jrPressure import JrPressure

# setup logging
LOG_FILE = '/home/robert/jrWetterstation/logs/jrWetterstation.log'
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s-%(module)s-%(lineno)s-%(levelname)s-%(message)s',
                    datefmt='%y%m%d-%H%M%S',
                    level=logging.INFO)
logging.info("jrAlert started")

RDD_FILE = '/home/robert/jrWetterstation/db/jrWetter.rrd'
OBSERVATION_TIME = 3  # time in hours
PRESS_DELTA_NORMAL = 1.5  # value in hPA per OBSERVATION_PERIOD
PRESS_DELTA_STRONG = 3.0  # value for storm warning (same period as above)

observationStr = '-' + str(OBSERVATION_TIME) + 'hr'
# rrdResult = rrdtool.fetch(RDD_FILE, 'AVERAGE', '-s -4hr')
rrdResult = rrdtool.fetch(RDD_FILE, "AVERAGE", "-s" + observationStr)
valueList = rrdResult[2]
firstPressValue = None
lastPressValue = None
for value in valueList:
    if value[1] is not None:
        if firstPressValue is None:
            firstPressValue = value[1]
        lastPressValue = value[1]

assert firstPressValue is not None
press = JrPressure()
press.set(lastPressValue)
diffPress = lastPressValue - firstPressValue
press.mod_status(diffPress)

logMsg = ('Press: ' + str(lastPressValue) +
          ' Diff: ' + str(diffPress) +
          " Average change per hour for last " +
          str(OBSERVATION_TIME) + " hours: " +
          str(diffPress / OBSERVATION_TIME))
logging.info(logMsg)
