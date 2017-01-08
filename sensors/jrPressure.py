import json

PRESS_STATUS_FILE = "pressStatus.json"

PRESS_SONNIG = 1
PRESS_BEWOELKT = 2
PRESS_REGNERISCH = 3
PRESS_STURM = 4


class JrPressure:
    # =================================================================================================================
    def __init__(self):
        self.__status = PRESS_BEWOELKT
        with open(PRESS_STATUS_FILE, 'w') as outfile:
            json.dump(self.__status, outfile)

        # get press status from PRESS_STATUS_FILE via json.load
        with open(PRESS_STATUS_FILE) as infile:
            data = json.load(infile)
    # =================================================================================================================
    def mod_status(self, value):
        print(self.__press_status)
        print(value)

    # =================================================================================================================
    def __del__(self):
        with open(PRESS_STATUS_FILE, 'w') as outfile:
            json.dump(self.__status, outfile)
