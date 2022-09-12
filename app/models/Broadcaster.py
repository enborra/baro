import requests


class Broadcaster():



    def __init__(self, *args, **kwargs):


        pass

    def cycle(self, *args, **kwargs):
        # t = kwargs['temp']
        t = '0'

        r = requests.get('http://admin.gingerbee.co/api/temp?t='+t+'&h=3&b=2')
        # pass
