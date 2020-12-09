DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS album;

CREATE TABLE artist (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE album (
    id SERIAL PRIMARY KEY,
    album_name VARCHAR(255),
    artist VARCHAR(255)
);
