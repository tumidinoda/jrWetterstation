import sys
import logging
from datetime import datetime
from Mail import Mail
import rrdtool

class KY015_Sensor:    
#=======================================================================================================================
    def __init__(self):
        self.hoehe=166 #Hoehe Seyring
        self.lastTemp = -99.0
        self.actTemp = -99.0
        self.minTemp=99.9
        self.maxTemp=-99.9
        self.lastPress = 0.0
        self.actPress = 0.0
        self.minPress=2000
        self.maxPress=0.0

        self.myLogger=logging.getLogger('jrWetterstationLogger')
        self.myLogger.debug('KY053 constructor started')

        retrytime=1 #sec 
        while True:
            try:
                # Sensor wird initialisiert
                self.myLogger.debug('BMP085 initialisieren')
                self.BMPSensor = BMP085.BMP085()
                success=True
                self.myLogger.debug('KY-053 sensor successful created')
                break
            except IOError:
                self.myLogger.debug('KY-053 sensor not detected. Check wiring. Try again in: '+str(sleeptime)+' seconds')
                print ("KY-053 Sensor nicht erkannt!")
                print ("Ueberpruefen Sie die Verbindungen")
                print ("Naechste Versuch in: "+str(sleeptime)+" Sekunden")
                time.sleep(retrytime)
                retrytime*=3

        self.myLogger.debug('KY053 constructor ended')
#=======================================================================================================================
    def read(self):
        self.actTemp=self.BMPSensor.read_temperature()
        press=self.BMPSensor.read_pressure()/100.0
        #Umrechnen auf Meereshoehe
        self.actPress=press/pow(1.0-self.hoehe/44330.0,5.255)
        self.actPress=round(self.actPress,2)
#=======================================================================================================================
    def out(self):
        print '---------------------------------------'
        print "Temperatur:", self.actTemp, "°C"
        print "Druck:", self.actPress, "hPa"
#=======================================================================================================================
    def save(self):
	#write values to round robin DB
	rrdtool.update('jrWetter.rrd','N:%s:%s' %(self.actTemp,self.actPress))
	#print cmd
        #rrdtool.update(cmd)	

        # save only if diff greater than delta
        deltaTemp=0.5
        if (self.actTemp<self.minTemp): self.minTemp=self.actTemp
        if (self.actTemp>self.maxTemp): self.maxTemp=self.actTemp
        if (self.actTemp < self.lastTemp-deltaTemp) or (self.actTemp > self.lastTemp+deltaTemp):
            #eliminate jitter (diff > 10 degrees)
            if abs(self.actTemp-self.lastTemp) < 10: 
                self.myLogger.info('TempChange: '+str(self.actTemp)+' Druck: '+str(self.actPress))
                #write to db
                con = sql.connect('Wetterstation.db')
                with con:    
                    cur = con.cursor()
                    cur.execute("INSERT INTO tempLogs(temperatur) VALUES(?)",(self.actTemp,))
                con.commit()
                con.close()
                #send Mail to Robert
                myMail=Mail()
                myMail.sendTempMail(self.actTemp,self.minTemp,self.maxTemp)
            else:
                self.myLogger.debug('Temperatur jitter: actTemp: '+str(self.actTemp)+' lastTemp: '+str(self.lastTemp))
            self.lastTemp=self.actTemp

        deltaPress=1
        if (self.actPress<self.minPress): self.minPress=self.actPress
        if (self.actPress>self.maxPress): self.maxPress=self.actPress
        if (self.actPress<self.lastPress-deltaPress) or (self.actPress>self.lastPress+deltaPress):
            self.myLogger.info('Temp: '+str(self.actTemp)+' DruckChange: '+str(self.actPress))
            self.lastPress=self.actPress
            myMail=Mail()
            myMail.sendPressMail(self.actPress,self.minPress,self.maxPress)


