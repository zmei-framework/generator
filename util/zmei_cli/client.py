import os
from json import JSONDecodeError

import jwt
import time
import requests


class ApiError(Exception):
    def __init__(self, response, *args) -> None:
        super().__init__(*args)
        self.response = response

    def __str__(self) -> str:
        ret = f'Error happened during API request: {self.response.status_code}. '

        if self.response.status_code != 404:
            ret += self.response.content.decode()
        else:
            ret += self.response.request.url

        return ret


class JsonError(ApiError):

    def __str__(self) -> str:
        return f"Can not parse server response, json expected: {self.response.content}"


class ZmeiApiClient(object):
    def __init__(self, api_url, apps_url) -> None:
        super().__init__()

        self.api_url = api_url
        self.apps_url = apps_url
        self.token = None

    def format_headers(self, service):
        if service == 'login':
            headers = {}
        else:
            headers = {'Authorization': f'JWT {self.get_token()}'}

        return headers

    def _request(self, method, service, kwargs, json=False):
        response = method(
            self.get_service_url(service),
            headers=self.format_headers(service),
            **kwargs
        )
        self.handle_response(method, service, response, **kwargs)

        if json:
            try:
                return response.json()
            except JSONDecodeError as e:
                raise JsonError(response)
        else:
            return response

    def _get_json(self, service, **kwargs):
        return self._request(requests.get, service, kwargs, json=True)

    def _post_json(self, service, **kwargs):
        return self._request(requests.post, service, kwargs, json=True)

    def _get(self, service, **kwargs):
        return self._request(requests.get, service, kwargs)

    def _post(self, service, **kwargs):
        return self._request(requests.post, service, kwargs)

    def _delete(self, service, **kwargs):
        return self._request(requests.delete, service, kwargs)

    def get_service_url(self, service):
        if service == 'generate':
            return f'{self.api_url}{service}'
        elif service == 'login':
            return f'{self.apps_url}api-token-auth/'
        elif service == 'refresh':
            return f'{self.apps_url}api-token-refresh/'
        else:
            return f'{self.apps_url}{service}/'

    def handle_response(self, method, service, response, **kwargs):
        if response.status_code >= 400:
            raise ApiError(response)

        return response

    def get_token(self):
        if not self.token:
            try:
                with open(os.path.expanduser('~/.zmei/token')) as f:
                    token = f.read()
                    data = jwt.decode(token, verify=False)

                    delta = data['exp'] - int(time.time())
                    if delta < 5:
                        print('Session expired. Logout.')
                        return

                    self.token = token

                    if delta < 10:  # 1 hour
                        self.refresh_token()

            except FileNotFoundError:
                self.token = None

        return self.token

    def is_logged_in(self):
        return self.get_token() is not None

    def refresh_token(self):
        try:
            print('Refreshing auth token')
            self.token = self._post_json('refresh', data={
                'token': self.token,
            })['token']

            path = os.path.expanduser('~/.zmei/token')
            with open(path, 'w') as f:
                f.write(self.token)

            return True

        except ApiError as e:
            print("Error happened during token refersh")
            if 'non_field_errors' in e.response:
                print('\n'.join(e.response['non_field_errors']))
            else:
                print(e.response)

            return False

    def login(self, email, password):
        try:
            self.token = self._post_json('login', data={
                'email': email,
                'password': password
            })['token']

            path = os.path.expanduser('~/.zmei/token')
            dirname = os.path.dirname(path)
            if not os.path.exists(dirname):
                os.makedirs(dirname, mode=0o700)

            with open(path, 'w') as f:
                f.write(self.token)
            os.chmod(path, 0o600)

            print('Successfully logged in!')

            return True

        except ApiError as e:
            print('\n'.join(e.response.json()['non_field_errors']))

            return False

    def logout(self):
        try:
            os.unlink(os.path.expanduser('~/.zmei/token'))
        except FileNotFoundError:
            pass

        self.token = None

        print('Logged out!')

    def generate(self, files, collections=None):
        response = self._post('generate', data={
            'collections': ','.join(collections),
        }, files={
            'gen': files
        })

        return response.content

    def app_get(self, **filter):
        found = self.app_list(**filter)
        if found:
            return found[0]

    def app_list(self, **filter):
        return self._get_json('api/application', params=filter)

    def app_create(self, ref, key):
        return self._post_json('api/application_new', data={
            'ref': ref,
            'key': key
        })

    def app_delete(self, ref=None, app_id=None):
        apps = self.app_list(ref=ref, id=app_id)
        if not len(apps):
            return False

        for app in apps:
            self._delete(f"api/application_new/{app['id']}")

        return True

    def ssh_key_list(self, **filter):
        return self._get_json('api/ssh_key', params=filter)

    def ssh_key_create(self, name, key):
        return self._post_json('api/ssh_key', data={
            'name': name,
            'key': key,
        })

    def ssh_key_delete(self, name=None, ssh_key_id=None):
        ssh_keys = self.ssh_key_list(name=name, id=ssh_key_id)
        if not len(ssh_keys):
            return False

        for ssh_key in ssh_keys:
            self._delete(f"api/ssh_key/{ssh_key['id']}")

        return True
