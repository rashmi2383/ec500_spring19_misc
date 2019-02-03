class Message(object):
    def __init__(self, content):
        self._content = content

    def get_msg_content(self):
        return self._content


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
    def __init__(self, systollic, diastollic):
        self._systollic = systollic
        self._diastollic = diastollic

    def get_systollic(self):
        return self._systollic

    def get_diastollic(self):
        return self._diastollic




