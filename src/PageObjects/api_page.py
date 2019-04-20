import requests

from src.api_constants import USERNAME, PASSWORD

BASE_URL = 'http://localhost:8080/authorization'


class Api:

    @staticmethod
    def login_api(username, password):
        params = {USERNAME: username, PASSWORD: password}
        return Api.post_params(params, BASE_URL).cookies

    @staticmethod
    def post_params(params, url, cookies=None):
        return requests.request('POST', url, json=params, cookies=cookies)

    @staticmethod
    def put_params(params, url, cookies=None):
        return requests.request('PUT', url, json=params, cookies=cookies)

    @staticmethod
    def delete_params(url, cookies=None):
        return requests.request('DELETE', url, json=params, cookies=cookies)
