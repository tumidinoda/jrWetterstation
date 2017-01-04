import rrdtool
rrdResult = rrdtool.fetch("../db/jrWetter.rrd", 'AVERAGE', '-s -2hr')
n = rrdResult[2]
p = 0 
for p in range(len(n)):
    s = n[p]
#    print s
    first = s[0]
#    print first
    second = s[1]
    print str(first) + " " + str(second)
p = p + 1
