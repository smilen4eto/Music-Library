import json


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        songs_remove = []
        for song in self.songs:
            if song_name == song.title:
                songs_remove.append(song)
        for song in songs_remove:
            self.songs.remove(song)

    def total_length(self):
        length = 0
        for song in self.songs:
            length += song.length
        return length

    def remove_disrated(self, rating):
        songs_remove = []
        for song in self.songs:
            if int(song.rating) < int(rating) + 1:
                songs_remove.append(song)
        for song in songs_remove:
            self.songs.remove(song)

    def remove_bad_quality(self):
        songs_remove = []
        for song in self.songs:
            if int(song.bitrate) < 400:
                songs_remove.append(song)
        for song in songs_remove:
            self.songs.remove(song)

    def show_artists(self):
        artist_set = set()
        for song in self.songs:
            artist_set.add(song.artist)
        return artist_set

    def str(self):
        playlist_str = []
        for song in self.songs:
            playlist_str.append(("{} {} - {}").format(song.artist ,song.title ,song.length))
        return playlist_str

    def jdefault(self):
        return self.songs.__dict__
