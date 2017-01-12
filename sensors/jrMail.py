import logging
import netrc
import smtplib
import time
from datetime import datetime


# noinspection PyPep8Naming
class JrMail:
    # =======================================================================================================================
    def __init__(self):
        self.__address = 'robert.jonas@gmx.at'
        self.__smtpserver = 'mail.gmx.net'
        self.__user = 'robert.jonas@gmx.at'
        self.__pw = 'Seyring4'
        self.myLogger = logging.getLogger('jrWetterstationLogger')
        self.myLogger.debug('Mail constructor')

        secrets = netrc.netrc()
        self.__user, self.__address, self.__pw = secrets.authenticators(self.__smtpserver)

    # =======================================================================================================================
    def sendTempMail(self, actTemp, minTemp, maxTemp):
        inhalt = 'Aktuelle Temperatur: ' + str(actTemp)
        inhalt += ' Minimum: ' + str(minTemp)
        inhalt += ' Maximum: ' + str(maxTemp)
        inhalt += ' ' + str(datetime.now())

        text = 'From: ' + self.__address + '\n'
        text += 'To: ' + self.__address + '\n'
        text += 'Date: ' + time.ctime(time.time()) + '\n'
        text += 'Subject: Temperatur\n\n'
        text += inhalt

        self.myLogger.debug(text)

        server = smtplib.SMTP_SSL(self.__smtpserver)
        server.login(self.__user, self.__pw)
        server.sendmail(self.__address, self.__address, text)
        server.quit()

    # =======================================================================================================================
    def sendPressMail(self, actPress, minPress, maxPress):
        inhalt = 'Aktueller Druck: ' + str(actPress)
        inhalt += ' Minimum: ' + str(minPress)
        inhalt += ' Maximum: ' + str(maxPress)
        inhalt += ' ' + str(datetime.now())

        text = 'From: ' + self.__address + '\n'
        text += 'To: ' + self.__address + '\n'
        text += 'Date: ' + time.ctime(time.time()) + '\n'
        text += 'Subject: Druck\n\n'
        text += inhalt

        self.myLogger.debug(text)

        server = smtplib.SMTP_SSL(self.__smtpserver)
        server.login(self.__user, self.__pw)
        server.sendmail(self.__address, self.__address, text)
        server.quit()

    # =======================================================================================================================
    def sendMail(self, subject, inhalt):
        text = 'From: ' + self.__address + '\n'
        text += 'To: ' + self.__address + '\n'
        text += 'Date: ' + time.ctime(time.time()) + '\n'
        text += 'Subject: ' + subject + '\n\n'
        text += inhalt

        self.myLogger.debug(text)

        server = smtplib.SMTP_SSL(self.__smtpserver)
        server.login(self.__user, self.__pw)
        server.sendmail(self.__address, self.__address, text)
        server.quit()

# =======================================================================================================================
