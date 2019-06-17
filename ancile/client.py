"""
"""
from requests import post
from ancile.errors import AncileException, PolicyException

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

    def execute(self, program, url=None, purpose=None, user=None, users=None):
        url = url or self.url
        purpose = purpose or self.purpose
        users = [user] if user else users

        if not url:
            raise ValueError("No API URL specified")
        
        if not purpose:
            raise ValueError("No purpose specified")
        
        if not users:
            raise ValueError("No users specified")
        
        request_json = {
            "token": token
            "program": program,
            "purpose": purpose,
            "users": users,
        }

        ancile_response = post(url, json=request_json).json()

        if ancile_response["status"] != "ok":
            if "Policy" in self.ancile_response["error"]:
                raise PolicyException
            
            else:
                raise AncileException

        return ancile_response["data"]
