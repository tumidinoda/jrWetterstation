import logging
import rrdtool
from jrMail import JrMail

RDD_FILE = '/home/robert/jrWetterstation/db/jrWetter.rrd'
OBSERVATION_TIME = 3  # time in hours
PRESS_DELTA_NORMAL = 2  # value in hPA per OBSERVATION_TIME
PRESS_DELTA_STRONG = 4  # value for storm warning (same period as above)

# myLogger=logging.getLogger('jrWetterstationLogger')
# myLogger.info('jrAlert started')

observation_str = '-' + str(OBSERVATION_TIME) + 'hr'
# rrdResult = rrdtool.fetch(RDD_FILE, 'AVERAGE', '-s -4hr')
rrdResult = rrdtool.fetch(RDD_FILE, 'AVERAGE', '-s' + observation_str)
valueList = rrdResult[2]
firstPressValue=None
lastPressValue=None
for value in valueList:
    if value[1] is not None:
        if firstPressValue is None:
            firstPressValue=value[1]
        lastPressValue = value[1]

assert firstPressValue is not None
diffPress=lastPressValue-firstPressValue
print("Diff: " + str(diffPress) +
      " Average change per hour for last " +
      str(OBSERVATION_TIME) + " hours: " +
      str(diffPress / OBSERVATION_TIME))

myMail = JrMail()
mailStr = "DruckVorher: " + str(firstPressValue) + " DruckJetzt: " + str(lastPressValue) + "\n"
if abs(diffPress) >= PRESS_DELTA_NORMAL:
    if abs(diffPress)>=PRESS_DELTA_STRONG:
        mailStr += "Starke Druckänderung"
    else:
        mailStr += "Leichte Druckänderung"
    myMail.sendMail('Druckaenderung', mailStr)
