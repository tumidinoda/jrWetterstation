import time
import smtplib
import logging
from datetime import datetime

class jrMail():    
#=======================================================================================================================
    def __init__(self):
        self.adress='robert.jonas@gmx.at'
        self.smtpserver='mail.gmx.net'
        self.user='robert.jonas@gmx.at'
        self.pw='Seyring4'
        self.myLogger=logging.getLogger('jrWetterstationLogger')
        self.myLogger.debug('Mail constructor')
#=======================================================================================================================
    def sendTempMail(self,actTemp,minTemp,maxTemp):
        inhalt='Aktuelle Temperatur: '+str(actTemp)
        inhalt+=' Minimum: '+str(minTemp)
        inhalt+=' Maximum: '+str(maxTemp)
        inhalt+=' '+str(datetime.now())
        
        text='From: '+self.adress+'\n'
        text+='To: '+self.adress+'\n'
        text+='Date: '+time.ctime(time.time())+'\n'
        text+='Subject: Temperatur\n\n'
        text+=inhalt

        self.myLogger.debug(text)

        server=smtplib.SMTP_SSL(self.smtpserver)
        server.login(self.user,self.pw)
        server.sendmail(self.adress,self.adress,text)
        server.quit()
#=======================================================================================================================
    def sendPressMail(self,actPress,minPress,maxPress):
        inhalt='Aktueller Druck: '+str(actPress)
        inhalt+=' Minimum: '+str(minPress)
        inhalt+=' Maximum: '+str(maxPress)
        inhalt+=' '+str(datetime.now())
        
        text='From: '+self.adress+'\n'
        text+='To: '+self.adress+'\n'
        text+='Date: '+time.ctime(time.time())+'\n'
        text+='Subject: Druck\n\n'
        text+=inhalt

        self.myLogger.debug(text)

        server=smtplib.SMTP_SSL(self.smtpserver)
        server.login(self.user,self.pw)
        server.sendmail(self.adress,self.adress,text)
        server.quit()
#=======================================================================================================================
    def sendMail(self,subject,msg):
        inhalt=msg
            
        text='From: '+self.adress+'\n'
        text+='To: '+self.adress+'\n'
        text+='Date: '+time.ctime(time.time())+'\n'
        text+='Subject: '+subject + '\n\n'
        text+=inhalt

        self.myLogger.debug(text)

        server=smtplib.SMTP_SSL(self.smtpserver)
        server.login(self.user,self.pw)
        server.sendmail(self.adress,self.adress,text)
        server.quit()
#=======================================================================================================================