import logging
import rrdtool
from jrMail import JrMail

# setup logging
logging.basicConfig(format='%(asctime)s-%(module)s-%(lineno)s-%(levelname)s-%(message)s',
                    datefmt='%y%m%d-%H%M%S',
                    level=logging.INFO)
logging.info("jrAlert started")

RDD_FILE = '/home/robert/jrWetterstation/db/jrWetter.rrd'
OBSERVATION_TIME = 3  # time in hours
PRESS_DELTA_NORMAL = 2  # value in hPA per OBSERVATION_TIME
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

myMail = JrMail()
mailMsg = "DruckVorher: " + firstPressValue + " DruckJetzt: " + lastPressValue + "\n"
if abs(diffPress) >= PRESS_DELTA_NORMAL:
    if abs(diffPress) >= PRESS_DELTA_STRONG:
        mailMsg += "Starke Druckänderung"
    else:
        mailMsg += "Leichte Druckänderung"
    myMail.sendMail('Druckaenderung', mailMsg)
