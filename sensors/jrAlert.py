import rrdtool
rrdResult = rrdtool.fetch("../db/jrWetter.rrd", 'AVERAGE', '-s -2hr')
print (rrdResult)
valueList = rrdResult[2]
diffPress = 0
oldPress = valueList[0][1]
numPress = 0
for value in valueList:
    print (str(value[0]) + ' ' + str(value[1]))
    if value[1] != None:    
       diffPress += (value[1]-oldPress)
       oldPress = value[1]
       numPress += 1

print("Diff: " + str(diffPress) +
      " Iter: " + str(numPress) +
      " Change: " + str(diffPress/numPress))



"""
for i in range(len(valueList)):
    valueTupel = valueList[i]
    temp0 = valueTupel[0]
    press0 = valueTupel[1]
    print (str(temp0) + " " + str(press0))
    diffPress+=(oldPress-press0)
    print (diffPress)
    oldPress=press0
"""
