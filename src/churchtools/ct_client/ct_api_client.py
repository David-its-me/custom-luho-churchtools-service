
import ast
import json
import logging
from datetime import datetime
import os
import requests
from typing import Optional
logger = logging.getLogger(__name__)
from churchtools_api.churchtools_api_abstract import ChurchToolsApiAbstract

class CTApiClient(ChurchToolsApiAbstract):

    def __init__(self) -> None:
        super().__init__()
        self._session = None
        self._token = None
        self._users = None
        self._domain = None
        self._is_connection_established = False
    

    
    def open_connection(self):
        self.__load_connection_details()

        if self._token is not None:
            self.__login_ct_rest_api(ct_token=self._token)
        elif self.ct_user is not None and self.ct_password is not None:
            self.__login_ct_rest_api(ct_user=self.ct_user, ct_password=self.ct_password)

        logger.debug("Connection established")
        self._is_connection_established = True
    
    def get_domain_base_path(self) -> str:
        return self._domain

    def get_session(self):
        if not self._is_connection_established:
            raise Exception('Please open the connection first.')

        return self._session

    def __load_connection_details(self):
        if 'CT_TOKEN' in os.environ:
            self._token = os.environ['CT_TOKEN']
            self._domain = os.environ['CT_DOMAIN']
            users_string = os.environ['CT_USERS']
            self._users = ast.literal_eval(users_string)
            logging.info('using connection details provided with ENV variables')
        else:
            with open("secret/churchtools_credentials.json") as credential_file:
                secret_data = json.load(credential_file)
                self._token = secret_data["ct_token"]
                self._domain = secret_data["ct_domain"]
                self._users = secret_data["ct_users"]
            logging.info('using connection details provided from secrets folder')

    def __login_ct_rest_api(self, **kwargs):
        """Authorization: Login<token>
        If you want to authorize a request, you need to provide a Login Token as
        Authorization header in the format {Authorization: Login<token>}
        Login Tokens are generated in "Berechtigungen" of User Settings
        using REST API login as opposed to AJAX login will also save a cookie.

        :param kwargs: optional keyword arguments as listed
        :keyword ct_token: str : token to be used for login into CT
        :keyword ct_user: str: the username to be used in case of unknown login token
        :keyword ct_password: str: the password to be used in case of unknown login token
        :return: personId if login successful otherwise False
        :rtype: int | bool
        """
        self._session = requests.Session()

        if "ct_token" in kwargs:
            logger.info("Trying Login with token")
            url = self._domain + "/api/whoami"
            headers = {"Authorization": "Login " + kwargs["ct_token"]}
            response = self._session.get(url=url, headers=headers)

            if response.status_code == 200:
                response_content = json.loads(response.content)
                logger.info(
                    "Token Login Successful as %s",
                    response_content["data"]["email"],
                )
                self._session.headers["CSRF-Token"] = self.__get_ct_csrf_token()
                return json.loads(response.content)["data"]["id"]
            logger.warning(
                "Token Login failed with %s",
                response.content.decode(),
            )
            return False

        if "ct_user" in kwargs and "ct_password" in kwargs:
            logger.info("Trying Login with Username/Password")
            url = self._domain + "/api/login"
            data = {"username": kwargs["ct_user"], "password": kwargs["ct_password"]}
            response = self._session.post(url=url, data=data)

            if response.status_code == 200:
                response_content = json.loads(response.content)
                person = self._who_am_i()
                logger.info("User/Password Login Successful as %s", person["email"])
                return person["id"]
            logger.warning(
                "User/Password Login failed with %s",
                response.content.decode(),
            )
            return False
        return None
    
    def who_am_i(self):
        """Simple function which returns the user information for the authorized user
        :return: CT user dict if found or bool
        :rtype: dict | bool.
        """
        url = self._domain + "/api/whoami"
        response = self._session.get(url=url)

        if response.status_code == 200:
            response_content = json.loads(response.content)
            if "email" in response_content["data"]:
                logger.info("Who am I as %s", response_content["data"]["email"])
                return response_content["data"]
            logger.warning("User might not be logged in? %s", response_content["data"])
            return False
        logger.warning("Checking who am i failed with %s", response.status_code)
        return False
    
    def __get_ct_csrf_token(self):
        """Requests CSRF Token https://hilfe.church.tools/wiki/0/API-CSRF
        Storing and transmitting CSRF token in headers is required for all legacy AJAX API calls unless disabled by admin
        Therefore it is executed with each new login.

        :return: token
        :rtype: str
        """
        url = self._domain + "/api/csrftoken"
        response = self._session.get(url=url)
        if response.status_code == 200:
            csrf_token = json.loads(response.content)["data"]
            logger.debug("CSRF Token erfolgreich abgerufen %s", csrf_token)
            return csrf_token
        logger.warning(
            "CSRF Token not updated because of Response %s",
            response.content.decode(),
        )
        return None