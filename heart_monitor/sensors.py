from threading import Thread
from multiprocessing import Queue


class SensorReader(Thread):
    '''
    :developer Zeyu Fu
    This is the base class for the individual sensor, describing the basic operations.
    Later we can decide to forgo the base class and just define the derived classes

    :param data_source: object of class BloodPulseData | BloodOxygenData | BloodPressureData;
    :returns: uint32_t value of blood pulse | blood oxygen level | blood pressure
    :raises keyError: raises an exception

    :param display_handler: object of DisplayHandler, defining the display destination
    :returns: void function (Call display function to display updated data)
    :raises keyError: raises an exception

    :param out_queue: queue object from data processor
    :param check_interval: unsigned int value of reading interval (sec)
    :returns: queue object containing new data from sensors
    :raises keyError: raises an exception

    :param Table: database table
    :returns: void function (add new instance to data table)
    :raises keyError: raises an exception
    '''
    def read_sensor(data_source):
        return data_source.get()

    def update_display_component(display_handler):
        display_handler.display()

    def send_to_data_processor(out_queue, check_interval):
        out_queue.put(timeout=check_interval)
        return out_queue

    def update_database(Table):
        Table.add()


class BloodOxygenSensorReader(SensorReader):
    '''
    :developer: N/A
    This class decodes read data from a hardware sensor and forwards it the
    realtime data processor for vitals analysis. Additionally
    '''
    pass


class BloodPressureSensorReader(SensorReader):
    '''
    :developer: N/A
    This class decodes read data from a hardware sensor and forwards it the
    realtime data processor for vitals analysis. Additionally
    '''
    pass


class BloodPulseReader(SensorReader):
    '''
    :developer: N/A
    This class decodes read data from a hardware sensor and forwards it the
    realtime data processor for vitals analysis. Additionally
    '''
    pass
