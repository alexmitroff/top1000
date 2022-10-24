import csv

from .track import Track


class Top:
    def __init__(self):
        self.top = {}

    def add_track(self, csv_track):
        track = Track(*csv_track)
        self.top[track.position] = track

    def as_JSON(self):
        serialized_list = {}
        for track in self.top.values():
            serialized_list[track.position] = track.as_JSON()
        return serialized_list

    def import_CSV(self, path_to_csv_file):
        with open(path_to_csv_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > 2:
                    self.add_track(row)
