from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artist (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [artist.first_name, artist.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artist"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['first_name'], row['last_name'], row['id'])
        artists.append(artist)
    return artist

def select(id):
    artist = None
    sql = "SELECT * FROM artist WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['first_name'], result['last_name'], result['id'])
    return artist

def delete_all():
    sql = "DELETE FROM artist"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artist WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(artist):
    sql = "UPDATE artists SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [artist.first_name, artist.last_name, artist.id]
    run_sql(sql, values)

# def tasks(artist):
#     tasks = []

#     sql = "SELECT * FROM tasks WHERE user_id = %s"
#     values = [user.id]
#     results = run_sql(sql, values)

    # for row in results:
    #     task = Task(row['description'], user, row['duration'], row['completed'], row['id'])
    #     tasks.append(task)
    # return tasks
