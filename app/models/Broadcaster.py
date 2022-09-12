import requests


class Broadcaster():
    _broadcast_interval = 1
    _interval_count = 0


    def __init__(self, *args, **kwargs):
        pass

    def cycle(self, *args, **kwargs):

        if self._interval_count > self._broadcast_interval:
            t = str(kwargs['temp'])
            # t = '0'

            r = requests.get('http://admin.gingerbee.co/api/temp?t='+t+'&h=3&b=2')

            self._interval_count = 0

        else:
            self._interval_count += 1
