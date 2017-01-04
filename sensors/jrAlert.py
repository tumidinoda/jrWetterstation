rrdResult = rrdtool.fetch("jrWetter.rrd", 'AVERAGE', '-s -2hr')
n = rrdResult[2]
p = 0 for p in range(len(n)):
    s = n[p]
    print s
    first = s[0]
    print first
    second = s[1]
    print second
p = p + 1
