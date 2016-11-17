#!/bin/bash
sleep 30
sudo /usr/bin/python -u /home/robert/jrWetterstation/projektWetterstation.py>>/home/robert/jrWetterstation/myLogs.txt 2>&1 &
