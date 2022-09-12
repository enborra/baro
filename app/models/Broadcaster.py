import requests


class Broadcaster():



    def __init__(self, *args, **kwargs):


        pass

    def cycle(self, *args, **kwargs):
        r = requests.get('http://admin.gingerbee.co/api/temp?t='+kwargs.get('temp')+'&h=3&b=2')
        # pass
