import logging
import rrdtool
from jrMail import JrMail
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
PRESS_DELTA_NORMAL = 2  # value in hPA per OBSERVATION_PERIOD
PRESS_DELTA_STRONG = 4  # value for storm warning (same period as above)

observationStr = '-' + str(OBSERVATION_TIME) + 'hr'
# rrdResult = rrdtool.fetch(RDD_FILE, 'AVERAGE', '-s -4hr')
rrdResult = rrdtool.fetch(RDD_FILE, 'AVERAGE', '-s' + observationStr)
valueList = rrdResult[2]
firstPressValue = None
lastPressValue = None
for value in valueList:
    if value[1] is not None:
        if firstPressValue is None:
            firstPressValue = value[1]
        lastPressValue = value[1]

assert firstPressValue is not None
diffPress = lastPressValue - firstPressValue
logMsg = ('Diff: ' + str(diffPress) +
          " Average change per hour for last " +
          str(OBSERVATION_TIME) + " hours: " +
          str(diffPress / OBSERVATION_TIME))
logging.info(logMsg)

pressure = JrPressure()
myMail = JrMail()
mailMsg = "DruckVorher: " + str(firstPressValue) + " DruckJetzt: " + str(lastPressValue) + "\n"
if abs(diffPress) >= PRESS_DELTA_NORMAL:
    if abs(diffPress) >= PRESS_DELTA_STRONG:
        mailMsg += "Starke Druckänderung"
    else:
        mailMsg += "Leichte Druckänderung"
    myMail.sendMail('Druckaenderung', mailMsg)
    pressure.mod_status(diffPress)