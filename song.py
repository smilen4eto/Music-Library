class Song:
    MAX_RATING = 5
    MIN_RATING = 1

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rate):
        if rate < Song.MIN_RATING or rate > Song.MAX_RATING:
            raise ValueError("Rate must be between 0 and 5")
        else:
            self.rating = rate

