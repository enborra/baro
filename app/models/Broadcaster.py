import requests


class Broadcaster():
    _broadcast_interval = 3
    _interval_count = 0


    def __init__(self, *args, **kwargs):
        pass

    def cycle(self, *args, **kwargs):

        if self._interval_count > self._broadcast_interval:
            t = str(kwargs['temp'])
            h = str(kwargs['humidity'])
            b = str(kwargs['barometric'])
            # t = '0'

            r = requests.get( 'http://admin.gingerbee.co/api/temp?t='+t+'&h='+h+'&b='+b )

            self._interval_count = 0

        else:
            self._interval_count += 1
