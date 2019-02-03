
class DisplayHandler(object):

    '''
    :developer: Byoungsui Lee && Seunghee Lee
    This class receives numerical data from sensor readers and
    encodes the data for a display technology

    The displayhandler obejct will take in a object containing the vital data.
    Then it will parse the data into three catagories ( blood oxygen, blood pressure, pulse)
    Each of these parsed data will be the input for the three display methods.

    :param oxy: uint32_t value of blood oxygen level;
    returns: void function ( displays blood oxygen level )
    :raises keyError: raises an exception

    :param systolic: uint32_t value of blood pressure;
    :param diatolic: uint32_t value of blood pressure;
    returns: void function ( displays blood pressure level )
    :raises keyError: raises an exception

    :param pulse: uint32_t value of blood pulse;
    returns: void function ( displays pulselevel )
    :raises keyError: raises an exception
    '''
    def display_blood_oxygen(oxy):
    def display_blood_pressure(systolic,diatolic):
    def display_blood_pulse(pulse):


    pass


class TextTerminalDisplay(DisplayHandler):
    '''
    :developer: N/A
    A simple derived class which will print data to the terminal (stdout)
    '''