import requests


class Broadcaster():
    _broadcast_interval = 5
    _interval_count = 0


    def __init__(self, *args, **kwargs):
        pass

    def cycle(self, *args, **kwargs):

        if self._interval_count > self._broadcast_interval:
            t = str(kwargs['temp'])
            h = str(kwargs['humidity'])
            b = str(kwargs['barometric'])
            a_s = str(kwargs['air_small'])
            a_m = str(kwargs['air_medium'])
            a_l = str(kwargs['air_large'])
            # t = '0'

            r = requests.get( 'http://admin.gingerbee.co/api/temp?temp='+t+'&humidity='+h+'&barometric='+b+'&air_small='+a_s+'&air_medium='+a_m+'&air_large='+a_l )

            self._interval_count = 0

        else:
            self._interval_count += 1
