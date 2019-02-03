from enum import Enum


'''
The idea is that urgency can help the notification manager decided what
messaging medium is the most appropriate or if a message calls for multiple
mediums to be used
'''


class Urgency(Enum):
    LOW_URGENCY = 0
    MEDIUM_URGENCY = 1
    HIGH_URGENCY = 2


class Message(object):
    def __init__(self, content, urgency):
        self._content = content
        self._urgency = urgency

    def get_msg_content(self):
        return self._content

    def get_urgency(self):
        return self._urgency


class BloodPulseData(object):
    def __init__(self, pulse):
        self._pulse = pulse

    def get_pulse(self):
        return self._pulse


class BloodOxygenData(object):
    def __init__(self, oxy_level):
        self._oxy_level = oxy_level

    def get_oxy_data(self):
        return self._oxy_level


class BloodPressureData(object):
    def __init__(self, systolic, diastolic):
        self._systolic = systolic
        self._diastolic = diastolic

    def get_systolic(self):
        return self._systolic

    def get_diastolic(self):
        return self._diastolic


class Contact(object):
    def __init__(self, name, sms_info, telegram_info):
        self._name = name
        self._sms_info = sms_info
        self._telegram_info = telegram_info

    def get_name(self):
        return self._name

    def get_telegram(self):
        return self._telegram_info

    def get_sms(self):
        return self._sms_info
