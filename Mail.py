# -*- coding: utf-8 -*-
import time
import smtplib
from datetime import datetime

class Mail():    
#=======================================================================================================================
    def __init__(self):
        self.adress='robert.jonas@gmx.at'
        self.smtpserver='mail.gmx.net'
        self.user='robert.jonas@gmx.at'
        self.pw='Seyring4'
#=======================================================================================================================
    def send(self,actTemp,minTemp,maxTemp):
        inhalt='Aktuelle Temperatur: '+str(actTemp)
        inhalt+=' Minimum: '+str(minTemp)
        inhalt+=' Maximum: '+str(maxTemp)
        inhalt+=' '+str(datetime.now())
        
        text='From: '+self.adress+'\n'
        text+='To: '+self.adress+'\n'
        text+='Date: '+time.ctime(time.time())+'\n'
        text+='Subject: Temperatur\n\n'
        text+=inhalt

        print inhalt

        server=smtplib.SMTP_SSL(self.smtpserver)
        server.login(self.user,self.pw)
        server.sendmail(self.adress,self.adress,text)
        server.quit()

#=======================================================================================================================


