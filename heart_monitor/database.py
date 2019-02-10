import datetime
import display

class TextToDatabase:
    '''
    A simple derived class which will save data to dictionary with current timestamp
    '''

    def __init__(self,TextTerminalDisplay):
        self._cur_oxygen = TextTerminalDisplay._cur_oxygen
        self._cur_systolic = TextTerminalDisplay._cur_systolic
        self._cur_diastolic = TextTerminalDisplay._cur_diastolic
        self._cur_pulse = TextTerminalDisplay._cur_pulse
        self.save_data()

    def save_data(self):
        datetime_wise_data = {}
        timestamp = str(datetime.datetime.now())
        data = ''.join(
	    (
		'< {} bps HEART RATE > |' 
		'< {}/{} SYS/DIA mmHg kPa > |' 
		'< {}% Oxygen Saturation >'
            ).format(
                self._cur_pulse,
                self._cur_systolic,
                self._cur_diastolic,
                self._cur_oxygen
            )
	)
        datetime_wise_data[timestamp] = data
        print("Data: %s" % datetime_wise_data)
