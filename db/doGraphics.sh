#!/bin/sh
dbpath=$HOME/jrWetterstation/db

#1 Tag Auswertung
rrdtool graph jrWetter_1d.png --left-axis-format "%4.1lf" -w 900 -h 500 -E -A \
--right-axis 1:1014 --right-axis-format "%4.1lf" \
-t "Zimmertemperatur/Luftdruck last 24h" --end now --start end-1d \
DEF:temp=$dbpath/jrWetter.rrd:temp0:AVERAGE \
"LINE2:temp#0000ff:Zimmertemperatur\:" "GPRINT:temp:LAST:%2.1lf\n" \
DEF:press=$dbpath/jrWetter.rrd:press0:AVERAGE CDEF:druck=press,1014,- \
"LINE2:druck#ff0000:Luftdruck\:" "GPRINT:press:LAST:%2.1lf\n"

#7 Tage Auswertung
rrdtool graph jrWetter_7d.png --left-axis-format "%4.1lf" -w 900 -h 500 -E -A \
--right-axis 1:1014 --right-axis-format "%4.1lf" \
-t "Zimmertemperatur/Luftdruck last 7d" --end now --start end-7d \
DEF:temp=$dbpath/jrWetter.rrd:temp0:AVERAGE \
"LINE2:temp#0000ff:Zimmertemperatur\:" "GPRINT:temp:LAST:%2.1lf\n" \
DEF:press=$dbpath/jrWetter.rrd:press0:AVERAGE CDEF:druck=press,1014,- \
"LINE2:druck#ff0000:Luftdruck\:" "GPRINT:press:LAST:%2.1lf\n"

#30 Tage Auswertung
rrdtool graph jrWetter_30d.png --left-axis-format "%4.1lf" -w 900 -h 500 -E -A \
--right-axis 1:1014 --right-axis-format "%4.1lf" \
-t "Zimmertemperatur/Luftdruck last 30d" --end now --start end-30d \
DEF:temp=$dbpath/jrWetter.rrd:temp0:AVERAGE \
"LINE2:temp#0000ff:Zimmertemperatur\:" "GPRINT:temp:LAST:%2.1lf\n" \
DEF:press=$dbpath/jrWetter.rrd:press0:AVERAGE CDEF:druck=press,1014,- \
"LINE2:druck#ff0000:Luftdruck\:" "GPRINT:press:LAST:%2.1lf\n"

#transfer data to webserver
ftp wetterstation.jr1.at <<EOF
cd wetterstation.jr1.at
lcd $dbpath
prompt
mput *.png
quit
EOF
