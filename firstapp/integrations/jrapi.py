import os
import requests


class JrApi:
    API_URL = os.environ.get("API_URL", "https://instruct-api-teste.herokuapp.com/api/orgs/")

    def get_orgs(self):
        """
        Lista todas as organizações
        """
        return requests.get(f"{self.API_URL}").json()
    
    def create_and_get_org(self, org):
        """
        """
        return requests.get(f"{self.API_URL}{org}").json()

    def delete_org(self, org):
        """
        """
        return requests.delete(f"{self.API_URL}{org}")

    

