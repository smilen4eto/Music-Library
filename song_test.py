from song import Song

import unittest


class TestSong(unittest.TestCase):

    def setUp(self):
        self.new_song = Song("Wonderland", "Sunrise Avenue", "On the way to wonderland", 5, 220, 455)

    def test_song_init(self):
        self.assertEqual("Wonderland", self.new_song.title)
        self.assertEqual("Sunrise Avenue", self.new_song.artist)
        self.assertEqual("On the way to wonderland", self.new_song.album)
        self.assertEqual(5, self.new_song.rating)
        self.assertEqual(220, self.new_song.length)
        self.assertEqual(455, self.new_song.bitrate)

    def test_rate(self):
        with self.assertRaises(ValueError):
            self.new_song.rate(20)

if __name__ == '__main__':
    unittest.main()
