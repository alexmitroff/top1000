class Track:
    def __init__(self, position, artist, title, genries=[], year=None):
        self.position = int(position)
        self.artist = artist
        self.title = title
        self.genries = genries
        self.year = year

    def __str__(self):
        return f'{self.artist} - {self.title}'

    @property
    def csv_genries(self):
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
            self.csv_genries,
            self.year,
        ]

    def getherMeta(self):
        if self.year is not None:
            return
