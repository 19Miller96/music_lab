import pdb 
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist = Artist("Justin", "Timberlake")
artist_repository.save(artist)

artist = Artist("Beyonce", "Knowles")
artist_repository.save(artist)

