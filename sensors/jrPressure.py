# -*- coding: UTF-8 -*-
import json

from jrMail import JrMail

PRESS_STATUS_FILE = "/home/robert/jrWetterstation/sensors/pressStatus.json"

PRESS_SONNIG = 0
PRESS_BEWOELKT = 1
PRESS_REGNERISCH = 2
PRESS_STURM = 3
press_status = ('sonnig', 'bewoelkt', 'regnerisch', 'stuermisch')

PRESS_DELTA_NORMAL = 2  # value in hPA per OBSERVATION_PERIOD
PRESS_DELTA_STRONG = 4  # value for storm warning (same period as above)


class JrPressure:
    # =================================================================================================================
    def __init__(self):
        self.__value = 1013
        self.__status = PRESS_BEWOELKT
        # get press status from PRESS_STATUS_FILE via json.load
        with open(PRESS_STATUS_FILE) as infile:
            self.__status = json.load(infile)

    # =================================================================================================================
    def set(self, value):
        self.__value = value

    # =================================================================================================================
    def mod_status(self, diff):
        press_status_old = self.__status

        if diff >= PRESS_DELTA_NORMAL:
            if self.__status == PRESS_STURM:
                self.__status = PRESS_REGNERISCH
            elif self.__status == PRESS_REGNERISCH:
                self.__status = PRESS_BEWOELKT
            elif self.__status == PRESS_BEWOELKT:
                self.__status = PRESS_SONNIG

        if diff <= -PRESS_DELTA_NORMAL:
            if self.__status == PRESS_SONNIG:
                self.__status = PRESS_BEWOELKT
            elif self.__status == PRESS_BEWOELKT:
                self.__status = PRESS_REGNERISCH

        if diff <= -PRESS_DELTA_STRONG:
            self.__status = PRESS_STURM

        self.save()
        if press_status_old is not self.__status:
            self.__mail()

    # =================================================================================================================
    # noinspection PyPep8Naming
    def __mail(self):
        myMail = JrMail()
        mailMsg = str(round(self.__value, 2)) + " Es wird " + press_status[self.__status]
        myMail.sendMail("Wetterstation Druckaenderung", mailMsg)

    # =================================================================================================================
    def save(self):
        with open(PRESS_STATUS_FILE, 'w') as outfile:
            json.dump(self.__status, outfile)

    # =================================================================================================================
    def __del__(self):
        self.save()
