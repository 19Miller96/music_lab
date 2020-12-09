import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        self.album = Album("Justified", "Justin Timberlake")
    
    def test_album_has_name(self):
        self.assertEqual("Justified", self.album.album_name)

    def test_album_has_artist(self):
        self.assertEqual("Justin Timberlake", self.album.artist)