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
diffPress = 0
oldPress = valueList[0][
    1]  # assuming there is at least one value and this value is not None !  assert and catch exception t.b.d
for value in valueList:
    if value[1] is not None:
        diffPress += (value[1] - oldPress)
        oldPress = value[1]

print("Diff: " + str(diffPress) +
      " Average change per hour for last " +
      str(OBSERVATION_TIME) + " hours: " +
      str(diffPress / OBSERVATION_TIME))

myMail = jrMail()
mailStr = "DruckVorher: " + valueList[0][1] + " DruckJetzt: " + oldPress + "\n"
if abs(diffPress) >= 4:
    mailStr += "Starke Druckänderung"
else:
    mailStr += "Leichte Druckänderung"
myMail.sendMail('Druckaenderung', mailStr)
