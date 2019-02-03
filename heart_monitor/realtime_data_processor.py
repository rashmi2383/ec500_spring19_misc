import threading


class RealTimeDataProcessor(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        '''
        In here we need to process data we receive from sensor read queue.
        If any problems are detected in the attached patient's vitals
        we issue a command to the notification manager
        :return:
        '''
        raise NotImplementedError