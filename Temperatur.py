# -*- coding: utf-8 -*-
import glob
import time
from time import sleep
import RPi.GPIO as GPIO
import sqlite3 as sql
import sys
from datetime import datetime
from Mail import Mail

class Temperatur:    
#=======================================================================================================================
    def __init__(self):
        self.lastTemp = -99
        self.actTemp = -99
        self.minTemp=999
        self.maxTemp=-999
        # Der One-Wire EingangsPin wird deklariert und der integrierte PullUp-Widerstand aktiviert
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        base_dir = '/sys/bus/w1/devices/'
        while True:
            try:
                device_folder = glob.glob(base_dir + '28*')[0]
                break
            except IndexError:
                sleep(0.5)
                continue
        self.device_file = device_folder + '/w1_slave'
#=======================================================================================================================
    def read(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = TemperaturMessung()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            self.actTemp = int(temp_string) / 100
#=======================================================================================================================
    def out(self):
        print '---------------------------------------'
        print "Temperatur:", self.actTemp, "°C"

#=======================================================================================================================
    def save(self):
        if (self.actTemp<self.minTemp): self.minTemp=self.actTemp
        if (self.actTemp>self.maxTemp): self.maxTemp=self.actTemp
        if (self.actTemp > self.lastTemp-5) and (self.actTemp < self.lastTemp+5) : return
        #print str(datetime.now())," Act:",float(self.actTemp)/10.0,"last:",float(self.lastTemp)/10.0
        self.lastTemp=self.actTemp

        #write to db
        con = sql.connect('/var/www/html/Wetterstation.db')
        with con:    
            cur = con.cursor()
            cur.execute("INSERT INTO tempLogs(temperatur) VALUES(?)",(self.actTemp,))
        con.commit()
        con.close()
        myMail=Mail()
        myMail.send(float(self.actTemp)/10,float(self.minTemp)/10,float(self.maxTemp)/10)


