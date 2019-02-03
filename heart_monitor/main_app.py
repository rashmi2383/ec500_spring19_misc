import sensors
import prediction_engine
import realtime_data_processor


def main(cmd_args):
    '''
    Entry point of application; in here we spawn the sensor threads, AI thread and
    realtime data processing thread and then wait till we need to quit
    :param cmd_args: dictionary of expected command line arguments
    :return: 0 on success and non-zero on error
    '''