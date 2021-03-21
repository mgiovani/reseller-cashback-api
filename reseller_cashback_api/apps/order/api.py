import json

import requests
from prettyconf import config
from retrying import retry


class ExternalAPI():
    EXTERNAL_API_BASE_URL = config('EXTERNAL_API_BASE_URL')
    EXTERNAL_API_TOKEN = config('EXTERNAL_API_TOKEN')
    AUTHORIZATION = {'token': EXTERNAL_API_TOKEN}

    def _get_full_path(self, url):
        return f'{self.EXTERNAL_API_BASE_URL}{url}'

    def _get_formatted_response(self, response):
        try:
            return response.json()['body']
        except (KeyError, json.JSONDecodeError):
            return {'error': response.content}

    def _get_status_code(self, response):
        try:
            return response.json()['statusCode']
        except (KeyError, json.JSONDecodeError):
            return 500  # Server Error

    @retry(stop_max_attempt_number=5)
    def get(self, url, params={}):
        full_path = self._get_full_path(url)
        response = requests.get(
            full_path, headers=self.AUTHORIZATION, params=params)

        formatted_response = self._get_formatted_response(response)
        status_code = self._get_status_code(response)
        return formatted_response, status_code

    def get_accumulated_cashback(self, params):
        return self.get('cashback', params=params)
