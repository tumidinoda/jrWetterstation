#!/bin/bash
rrdtool create jrWetter.rrd --step 900 DS:temp0:GAUGE:1200:-40:80 DS:press0:GAUGE:1200:800:1200 RRA:AVERAGE:0.5:1:960 RRA:MIN:0.5:96:3600 RRA:MAX:0.5:96:3600 RRA:AVERAGE:0.5:96:3600