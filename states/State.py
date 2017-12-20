

class State(object):


    def __init__(self, id, v, pos):
        self._identificator = id
        self._value = v
        self._position = pos



    ############################################################################################
    ################################ Properties ################################################

    ##############################################
    ################ Identificator ###############
    ##############################################

    @property
    def identificator(self):
        return self._identificator


    @identificator.setter
    def identificator(self,value):
        self._identificator = value

    ##############################################
    ################### Value ####################
    ##############################################

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    ##############################################
    ################## Position ##################
    ##############################################

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    ############################################################################################
