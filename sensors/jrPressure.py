import pickle

PRESS_STATUS_FILE = "pressStatus.pkl"


class JrPressure:
    # =======================================================================================================================
    def __init__(self):
        # get press status from PRESS_STATUS_FILe via Pickle
        pkl_file = open(PRESS_STATUS_FILE, 'rb')
        self.__press_status = pickle.load(pkl_file)

    def mod_status(self, value):
        print(self.__press_status)
        print(value)
