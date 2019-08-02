"""
    The ancile client is reponsible for making
    requests to an ancile server and of reporting
    the response back to the user.
"""
from requests import post
from ancile.errors import AncileException, PolicyException
from ancile.utils import generate_url


class AncileClient:
    """
        Client responsible for making requests and receiving
        responses from ancile server. Needs ancile token
        and URL.

        :param token: Ancile API token
        :param url: Ancile instance root URL
    """

    def __init__(self, token, url):

        self.__token = token
        self.__url = generate_url(url)

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

    def execute(self, program, users):
        """
            Makes a POST request to the ancile server with your program and users.

            :param program: String of ancile program
            :param users: list of users
            :returns: response data from
        """
        request_json = {
            "token": self.__token,
            "program": program,
            "users": users,
        }

        ancile_response = post(self.__url, json=request_json).json()

        if ancile_response["result"] != "ok":
            if "Policy" in ancile_response["traceback"]:
                raise PolicyException(
                    "The policy prevented this program from executing."
                )

            raise AncileException(ancile_response["traceback"])

        return ancile_response["data"]
