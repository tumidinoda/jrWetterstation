#!/bin/sh
export PYTHONPATH=$PYTHONPATH:/home/robert
export LOG_CFG=/home/robert/jrPyCore/logs/jrLogger.yml
python /home/robert/jrWetterstation/sensors/jrWetterstation.py
