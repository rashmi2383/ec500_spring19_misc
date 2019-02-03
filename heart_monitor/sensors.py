from threading import Thread
from multiprocessing import Queue


class SensorReader(Thread):
    '''
    :developer Zeyu Fu
    This is the base class for the individual sensor, describing the basic operations.
    Later we can decide to forgo the base class and just define the derived classes
    '''
    pass


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