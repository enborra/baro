import requests


class Broadcaster():



    def __init__(self, *args, **kwargs):


        pass

    def cycle(self, values=None, *args, **kwargs):
        r = requests.get('http://admin.gingerbee.co/api/temp?t=5&h=3&b=2')
        # pass
