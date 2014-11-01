from playlist import Playlist
from song import Song

import unittest


class TestPlayslist(unittest.TestCase):

    def setUp(self):
        self.test_playlist = Playlist("My playlist")
        self.test_song = Song("Wonderland", "Sunrise Avenue", "On the way to wonderland", 5, 220, 255)

    def test_playlist_init(self):
        self.assertEqual("My playlist", self.test_playlist.name)

    def test_playlist_add_song(self):
        self.test_playlist.add_song(self.test_song)
        test_song2 = Song("Bla bla", "bla", "blaa", 1, 240, 412)
        test_song3 = Song("lala", "la", "laa", 2, 210, 478)
        self.test_playlist.add_song(test_song2)
        self.test_playlist.add_song(test_song3)
        self.assertIn(self.test_song, self.test_playlist.songs)
        self.assertIn(test_song2, self.test_playlist.songs)
        self.assertIn(test_song3, self.test_playlist.songs)

    def test_playlist_remove_song(self):
        test_song2 = Song("Bla bla", "bla", "blaa", 1, 240, 412)
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(test_song2)
        self.test_playlist.remove_song("Wonderland")
        self.assertNotIn(self.test_song, self.test_playlist.songs)
        self.assertIn(test_song2, self.test_playlist.songs)

    def test_total_length(self):
        test_song2 = Song("Bla bla", "bla", "blaa", 3, 240, 412)
        test_song3 = Song("lala", "la", "laa", 4, 210, 478)
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(test_song2)
        self.test_playlist.add_song(test_song3)
        self.assertEqual(self.test_playlist.total_length(), 670)

    def test_remove_disrated(self):
        test_song2 = Song("Bla bla", "bla", "blaa", 1, 240, 412)
        test_song3 = Song("lala", "la", "laa", 2, 210, 478)
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(test_song2)
        self.test_playlist.add_song(test_song3)
        self.test_playlist.remove_disrated(1)
        self.assertNotIn(test_song2, self.test_playlist.songs)

    def test_remove_bad_quality(self):
        test_song2 = Song("Bla bla", "bla", "blaa", 1, 240, 412)
        test_song3 = Song("lala", "la", "laa", 2, 210, 478)
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(test_song2)
        self.test_playlist.add_song(test_song3)
        self.test_playlist.remove_bad_quality()
        self.assertNotIn(self.test_song, self.test_playlist.songs)

    def test_show_artists(self):
        test_song2 = Song("Bla bla", "bla", "blaa", 1, 240, 412)
        test_song3 = Song("lala", "la", "laa", 2, 210, 478)
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(test_song2)
        self.test_playlist.add_song(test_song3)
        self.assertEqual({"Sunrise Avenue", "bla", "la"}, self.test_playlist.show_artists())

    def test_str(self):
        test_song2 = Song("Bla bla", "bla", "blaa", 1, 240, 412)
        test_song3 = Song("lala", "la", "laa", 2, 210, 478)
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(test_song2)
        self.test_playlist.add_song(test_song3)
        self.assertIn("Sunrise Avenue Wonderland - 220", self.test_playlist.str())

if __name__ == '__main__':
    unittest.main()
