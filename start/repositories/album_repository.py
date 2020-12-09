from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (album_name, artist) VALUES (%s, %s) RETURNING *"
    values = [album.album_name, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums= []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['album_name'], row['artist'], row['id'])
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['album_name'], result['artist'], result['id'])
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (album_name, artist) = (%s, %s) WHERE id = %s"
    values = [album.album_name, album.artist, album.id]
    run_sql(sql, values)
