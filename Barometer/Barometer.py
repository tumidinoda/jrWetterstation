#!/usr/bin/python
# coding=utf-8
# Copyright (c) 2014 Adafruit Industries
# Benoetigte Bibliotheken werden eingefügt und konfiguriert
import Adafruit_BMP.BMP085 as BMP085
import time

# Die Pause zwischen den Messungen kann hier eingestellt werden
sleeptime = 10

try:
    # Sensor wird initialisiert
    BMPSensor = BMP085.BMP085()
# Überprüfung ob Sensor richtig angeschlossen ist
# Falls nicht, wird eine Fehlermeldung ausgegeben
except IOError:
    print("------------------------------")
    print ("KY-053 Sensor nicht erkannt!")
    print ("Überprüfen Sie die Verbindungen")
    print("------------------------------")
    while(True):
        time.sleep(sleeptime)
except KeyboardInterrupt:
    GPIO.cleanup()

# Hauptprogrammschleife
# Das Programm startet die Messungen am Sensor und gibt
# die gemessenen Werte in der Konsole aus
try:
    while(1):
        print("------------------------------")
        # Temperatur
        print('Temperatur = {0:0.2f}°C'.format(BMPSensor.read_temperature()))
        # Luftdruck
        print('Luftdruck = {0:0.2f}hPa'.format(BMPSensor.read_pressure()/100))
        # Meereshöhe
        print('Meereshöhe = {0:0.2f}m'.format(BMPSensor.read_altitude()))
        print("------------------------------")
        print("")
        time.sleep(sleeptime)

# Aufraeumarbeiten nachdem das Programm beendet wurde
except KeyboardInterrupt:
    GPIO.cleanup()
