import json

PRESS_STATUS_FILE = "pressStatus.json"

PRESS_SONNIG = 1
PRESS_BEWOELKT = 2
PRESS_REGNERISCH = 3
PRESS_STURM = 4

PRESS_DELTA_NORMAL = 2  # value in hPA per OBSERVATION_PERIOD
PRESS_DELTA_STRONG = 4  # value for storm warning (same period as above)


class JrPressure:
    # =================================================================================================================
    def __init__(self):
        self.__status = PRESS_BEWOELKT
        # get press status from PRESS_STATUS_FILE via json.load
        with open(PRESS_STATUS_FILE) as infile:
            data = json.load(infile)
    # =================================================================================================================
    def mod_status(self, diffPress):
        if -diffPress>=PRESS_DELTA_STRONG:
            self.__status=PRESS_STURM
            self.save()
            return
        if diffPress>=PRESS_DELTA_NORMAL:
            if self.__status==PRESS_STURM:
                self.__status=PRESS_REGNERISCH
            elif

        if abs(diffPress) >= PRESS_DELTA_NORMAL:
            if abs(diffPress) >= PRESS_DELTA_STRONG:

    # =================================================================================================================
    def save(self):
        with open(PRESS_STATUS_FILE, 'w') as outfile:
            json.dump(self.__status, outfile)

    # =================================================================================================================
    def __del__(self):
        self.save()

