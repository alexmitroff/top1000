import os
import requests
from requests.auth import HTTPBasicAuth


class Spotify:
    def __init__(self, client_id, client_secret):
        """
        Auth response:
            {'access_token': '...', 'token_type': 'Bearer', 'expires_in': 3600}
        """
        self.token = None
        response = requests.post('https://accounts.spotify.com/api/token',
                                 auth=HTTPBasicAuth(client_id, client_secret),
                                 data={'grant_type': 'client_credentials'})

        if response.status_code < 200 or response.status_code > 299:
            print(f'Spotify response code {response.status_code}')
            return

        response = response.json()
        self.token = response['access_token']
        self.token_type = response['token_type']

    @staticmethod
    def process_request(string):
        strings = string.lower().split(' ')
        return ' '.join(strings)

    def search(self, artist, title, type='track', market=None, limit=None, offset=None):
        if not title or not artist:
            print("Empty query")
            return

        title = self.process_request(title)
        artist = self.process_request(artist)

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'{self.token_type} {self.token}'
        }

        params = {
            'q': title,
            'type': type,
        }

        if market is not None:
            params['market'] = market

        if limit is not None:
            params['limit'] = limit

        if offset is not None:
            params['offset'] = offset
        response = requests.get('https://api.spotify.com/v1/search',
                                headers=headers,
                                params=params)

        if response.status_code < 200 or response.status_code > 299:
            print(f'Search request returns {response.status_code}')
            return

        return response.json()


spotify_client = Spotify(os.getenv('SPOTIFY_CLIENTID'),
                         os.getenv('SPOTIFY_CLIENTSECRET'))
