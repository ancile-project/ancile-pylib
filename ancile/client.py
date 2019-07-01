"""
    The ancile client is reponsible for making
    requests to an ancile server and of reporting
    the response back to the user.
"""
from requests import post
from ancile.errors import AncileException, PolicyException

class AncileClient:
    """
        Client responsible for making requests and receiving
        responses from ancile server. Needs ancile token
        and URL.
    """

    def __init__(self, token, url, purpose):

        self.__token = token
        self.__url = url
        self.__purpose = purpose

    @property
    def token(self):
        """
            API token of the ancile app.
        """
        return self.__token

    @property
    def url(self):
        """
            ancile server URL
        """
        return self.__token

    @property
    def purpose(self):
        """
            the purpose of the ancile app
        """
        return self.__purpose

    def execute(self, program, users):
        """
            Makes a POST request to the ancile server with your program and users.

            :param program: String of ancile program
            :param users: list of users
            :return response data from
        """
        request_json = {
            "token": self.__token,
            "program": program,
            "purpose": self.__purpose,
            "users": users,
        }

        ancile_response = post(self.__url, json=request_json).json()

        if ancile_response["result"] != "ok":
            if "Policy" in ancile_response["traceback"]:
                raise PolicyException("The policy prevented this program from executing.")

            raise AncileException(ancile_response["traceback"])

        return ancile_response["data"]
