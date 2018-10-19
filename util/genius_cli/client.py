import sys
import zipfile
from io import BytesIO
from json.decoder import JSONDecodeError

import requests


class ApiError(Exception):
    def __init__(self, response, *args) -> None:
        super().__init__(*args)
        self.response = response


class GeniusClient(object):
    def __init__(self, api_url, token) -> None:
        super().__init__()

        self.api_url = api_url
        self.token = token

    def _get(self, service, **kwargs):
        headers = {'Authorization': f'Token {self.token}'}
        response = requests.get(f'{self.api_url}{service}', headers=headers, **kwargs)
        self.handle_error(service, response)
        return response.json()

    def _post(self, service, **kwargs):
        headers = {'Authorization': f'Token {self.token}'}
        url = f'{self.api_url}{service}'
        response = requests.post(url, headers=headers, **kwargs)
        self.handle_error(service, response)

        return response

    def handle_error(self, service, response):
        if response.status_code >= 400:
            try:
                error = response.json()

                print('')

                if 'detail' in error:
                    print(error['detail'])
                else:
                    print(error)

            except JSONDecodeError:
                print(
                    f'Http error {response.status_code}: Unexpected error happened on Genius server when working with /{service}.')
                print(response.content)

            raise ApiError(response)

    def generate(self, files, collections=None):
        response = self._post('generate', data={
            'collections': ','.join(collections),
        }, files={
            'gen': files
        })

        return response.content
