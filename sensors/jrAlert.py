import logging
import rrdtool
from jrMail import jrMail
RDD_FILE = '/home/robert/jrWetterstation/db/jrWetter.rrd'

#myLogger=logging.getLogger('jrWetterstationLogger')
#myLogger.info('jrAlert started')

rrdResult = rrdtool.fetch(RDD_FILE, 'AVERAGE', '-s -4hr')
valueList = rrdResult[2]
diffPress = 0
oldPress = valueList[0][1]    # assuming there is at least one value !  catch exception t.b.d
for value in valueList:
#    print (str(value[0]) + ' ' + str(value[1]))
    if value[1] is not None:    
       diffPress += (value[1]-oldPress)
       oldPress = value[1]
  
print("Diff: " + str(diffPress) +
      " Average change per hour for last 4 hours: " +
      str(diffPress/4))   # 4

myMail=jrMail()
myMail.sendMail('Druckaenderung ueber 4h',str(diffPress/4))


