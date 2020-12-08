import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    
    def setUp(self):
        self.artist = Artist("Justin", "Timberlake")
    
    def test_artist_has_first_name(self):
        self.assertEqual("Justin", self.artist.first_name)

    def test_artist_has_last_name(self):
        self.assertEqual("Timberlake", self.artist.last_name)
    
    