# -*- coding: UTF-8 -*-
import rrdtool
from time import sleep

from Adafruit_BMP import BMP085

from jrPyCore.jrLogger import JrLogger

LUFTDRUCKHOEHE = 166  # Hoehe Seyring


class KY015_Sensor:
    # =======================================================================================================================
    def __init__(self):
        self.hoehe = LUFTDRUCKHOEHE
        self.actTemp = -99.0
        self.actPress = 0.0

        self.my_logger = JrLogger().get()
        self.my_logger.debug('KY053 constructor started')

        retrytime = 1  # sec
        while retrytime < 100:
            try:
                # Sensor wird initialisiert
                self.my_logger.debug('BMP085 initialisieren')
                self.BMPSensor = BMP085.BMP085()
                self.my_logger.debug('KY-053 sensor successful created')
                break
            except IOError:
                self.my_logger.debug(
                    'KY-053 sensor not detected. Check wiring. Try again in: ' + str(retrytime) + ' seconds')
                print("KY-053 Sensor nicht erkannt!")
                print("Ueberpruefen Sie die Verbindungen")
                print("Naechste Versuch in: " + str(retrytime) + " Sekunden")
                sleep(retrytime)
                retrytime *= 3

    # =======================================================================================================================
    def read(self):
        self.actTemp = self.BMPSensor.read_temperature()
        press = self.BMPSensor.read_pressure() / 100.0
        # Umrechnen auf Meereshoehe
        self.actPress = press / pow(1.0 - self.hoehe / 44330.0, 5.255)
        self.actPress = round(self.actPress, 2)

    # =======================================================================================================================
    def out(self):
        print('---------------------------------------')
        print("Temperatur:", self.actTemp, "°C")
        print("Druck:", self.actPress, "hPa")

    # =======================================================================================================================
    def save(self):
        # write values to round robin DB
        rrdtool.update('jrWetter.rrd', 'N:%s:%s' % (self.actTemp, self.actPress))
        self.my_logger.info("Temp: " + str(self.actTemp) + " Press: " + str(self.actPress))
