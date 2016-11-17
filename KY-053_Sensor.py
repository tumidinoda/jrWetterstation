# -*- coding: utf-8 -*-
import Adafruit_BMP.BMP085 as BMP085
import time

class KY-053_Sensor:    
#=======================================================================================================================
    def __init__(self):
        self.lastTemp = -99
        self.actTemp = -99
        self.minTemp=999
        self.maxTemp=-999

	try:
		# Sensor wird initialisiert
		self.BMPSensor = BMP085.BMP085()
		# Überprüfung ob Sensor richtig angeschlossen ist
		# Falls nicht, wird eine Fehlermeldung ausgegeben
		except IOError:
			print("------------------------------")
			print ("KY-053 Sensor nicht erkannt!")
			print ("Überprüfen Sie die Verbindungen")
			print("------------------------------")
			while(True):
				time.sleep(1)
		except KeyboardInterrupt:
			GPIO.cleanup()
#=======================================================================================================================
    def read(self):
		self.actTemp=self.BMPSensor.read_temperature()
		self.actPress=self.BMPSensor.read_pressure()
#=======================================================================================================================
    def out(self):
        print '---------------------------------------'
        print "Temperatur:", self.actTemp, "°C"
        print "Druck:", self.actPress, "hPa"
#=======================================================================================================================
    def save(self):
        if (self.actTemp<self.minTemp): self.minTemp=self.actTemp
        if (self.actTemp>self.maxTemp): self.maxTemp=self.actTemp
        if (self.actTemp > self.lastTemp-5) and (self.actTemp < self.lastTemp+5) : return
        print str(datetime.now())," Act:",float(self.actTemp)/10.0,"last:",float(self.lastTemp)/10.0
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


