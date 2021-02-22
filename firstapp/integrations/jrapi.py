import os
import requests


class JrApi:
    API_URL = os.environ.get("API_URL", "https://instruct-api-teste.herokuapp.com/api/orgs/")

    def get_orgs(self):
        """Busca uma organização no Github
        :login: login da organização no Github
        """
        return requests.get(f"{self.API_URL}").json()

    

