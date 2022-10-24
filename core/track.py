class Track:
    def __init__(self, position, artist, title, genres=[], year=None):
        self.position = int(position)
        self.artist = artist
        self.title = title
        self.genres = genres
        self.year = year

    def __str__(self):
        return f'{self.artist} - {self.title}'

    @property
    def csv_genres(self):
        return ", ".join(self.genries)

    def as_JSON(self):
        return {
            'pos': self.position,
            'artist': self.artist,
            'title': self.title,
            'genries': self.genries,
            'year': self.year,
        }

    def as_CSV(self):
        return [
            self.position,
            self.artist,
            self.title,
            self.csv_genres,
            self.year,
        ]

    def getherMeta(self):
        if self.year is not None:
            return
        from spotify import spotify_client

        track_data = spotify_client.search(artist=self.artist, title=self.title, type='track')
        artist_id, self.year = self.get_release_date(track_data)

        artist_data = spotify_client.get_artist(artist_id)
        self.genres = self.get_genres(artist_data).split(',')

    def get_release_date(self, json_response):
        with open("/home/alex/Work/top1000/core/track.json") as jsonfile:
            import json
            json_response = json.loads(jsonfile.read())

        tracks = json_response['tracks']['items']
        artist_id = ""
        release_date_list = []
        for track in tracks:
            is_correct_title = self.title == track['name'].lower()
            # check track name
            if not is_correct_title:
                continue

            # check album type
            album = track['album']
            if album['album_type'] != 'album':
                continue

            # check artist name
            is_correct_artist = False
            for album_artist in album['artists']:
                if album_artist['name'].lower() == self.artist:
                    is_correct_artist = True
                    artist_id = album_artist['id']
                    break
            if not is_correct_artist:
                continue

            release_date = album['release_date']
            release_date_list.append(release_date)
        return artist_id, min(release_date_list)

    def get_genres(self, json_response):
        with open("/home/alex/Work/top1000/core/artist.json") as jsonfile:
            import json
            json_response = json.loads(jsonfile.read())

        return json_response['genres']

