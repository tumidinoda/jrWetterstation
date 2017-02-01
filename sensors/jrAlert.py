import rrdtool

from jrPressure import JrPressure
from jrPyCore.jrLogger import JrLogger

# setup logging
my_logger = JrLogger().setup(__name__)
my_logger.info("jrAlert started")

RDD_FILE = '/home/robert/jrWetterstation/db/jrWetter.rrd'
OBSERVATION_TIME = 3  # time in hours

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
my_logger.info(logMsg)
