import pdb 
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("Justin", "Timberlake")
artist_repository.save(artist_1)

artist_2 = Artist("Beyonce", "Knowles")
artist_repository.save(artist_2)

album_1 = Album("Justified", artist_1)
album_repository.save(album_1)

album_2 = Album("Lemonade", artist_2)
album_repository.save(album_2)

artist_3 = Artist("Michael", "Jackson")
artist_repository.save(artist_3)

album_3 = Album("Bad", artist_3)
album_repository.save(album_3)
