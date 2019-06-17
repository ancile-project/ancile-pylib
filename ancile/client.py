"""
"""

class AncileClient:

    def __init__(self, token, url=None, purpose=None):

        self.__token = token
        self.__url = url
        self.__purpose = purpose

    @property
    def token(self):
        return self.__token

    @property
    def url(self):
        return self.__token

    @property
    def purpose(self):
        return self.__purpose




