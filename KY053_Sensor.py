# -*- coding: utf-8 -*-
import Adafruit_BMP.BMP085 as BMP085
import time
import sqlite3 as sql
import sys
from datetime import datetime
from Mail import Mail

class KY053_Sensor:    
#=======================================================================================================================
    def __init__(self):
        self.lastTemp = -99.0
        self.actTemp = -99.0
        self.minTemp=99.9
        self.maxTemp=-99.9
        self.actPress=0.0

	try:
		# Sensor wird initialisiert
		self.BMPSensor = BMP085.BMP085()
		# Ueberpruefung ob Sensor richtig angeschlossen ist
		# Falls nicht, wird eine Fehlermeldung ausgegeben
	except IOError:
		print("------------------------------")
		print ("KY-053 Sensor nicht erkannt!")
		print ("Ueberpruefen Sie die Verbindungen")
		print("------------------------------")
		while(True):
			time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()
#=======================================================================================================================
    def read(self):
		self.actTemp=self.BMPSensor.read_temperature()
		self.actPress=self.BMPSensor.read_pressure()/100.0
#=======================================================================================================================
    def out(self):
        print '---------------------------------------'
        print "Temperatur:", self.actTemp, "°C"
        print "Druck:", self.actPress, "hPa"
#=======================================================================================================================
    def save(self):
        if (self.actTemp<self.minTemp): self.minTemp=self.actTemp
        if (self.actTemp>self.maxTemp): self.maxTemp=self.actTemp
        if (self.actTemp > self.lastTemp-0.5) and (self.actTemp < self.lastTemp+0.5) : return
#        print str(datetime.now())," Act:",self.actTemp,"last:",self.lastTemp
        self.lastTemp=self.actTemp

        #write to db
        con = sql.connect('Wetterstation.db')
        with con:    
            cur = con.cursor()
            cur.execute("INSERT INTO tempLogs(temperatur) VALUES(?)",(self.actTemp,))
        con.commit()
        con.close()
  
        #send Mail to Robert
        myMail=Mail()
        myMail.send(self.actTemp,self.minTemp,self.maxTemp,self.actPress)


