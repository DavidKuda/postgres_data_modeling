from TableProperties import TableProperties


users_properties = TableProperties('users',
                                   # [('user_id', 'TEXT PRIMARY KEY'),
                                   [('user_id', 'TEXT'),
                                    ('first_name', 'TEXT'),
                                    ('last_name', 'TEXT'),
                                    ('gender', 'TEXT'),
                                    ('level', 'TEXT')])

songs_properties = TableProperties('songs',
                                   # [('song_id', 'TEXT PRIMARY KEY'),
                                   [('song_id', 'TEXT'),
                                    ('title', 'TEXT'),
                                    # ('artist_id', 'TEXT REFERENCES artists(artist_id)'),
                                    ('artist_id', 'TEXT'),
                                    ('year', 'INT'),
                                    ('duration', 'DECIMAL')])

artists_properties = TableProperties('artists',
                                     # [('artist_id', 'TEXT PRIMARY KEY'),
                                     [('artist_id', 'TEXT'),
                                      ('name', 'TEXT'),
                                      ('location', 'TEXT'),
                                      ('latitude', 'DECIMAL'),
                                      ('longitude', 'DECIMAL')])

time_properties = TableProperties('time',
                                  [('start_time', 'TIMESTAMP'),
                                   ('hour', 'INT'),
                                   ('day', 'INT'),
                                   ('week', 'INT'),
                                   ('month', 'INT'),
                                   ('year', 'INT'),
                                   ('weekday', 'INT')])

songplays_properties = TableProperties('songplays',
                                       [('songplay_id', 'SERIAL PRIMARY KEY'),
                                        ('start_time', 'TIMESTAMP'),
                                        # ('user_id', 'TEXT REFERENCES users(user_id)'),
                                        ('user_id', 'TEXT'),
                                        ('level', 'TEXT'),
                                        # ('song_id', 'TEXT REFERENCES songs(song_id)'),
                                        ('song_id', 'TEXT'),
                                        # ('artist_id', 'TEXT REFERENCES artists(id)'),
                                        ('artist_id', 'TEXT'),
                                        ('session_id', 'TEXT'),
                                        ('location', 'TEXT'),
                                        ('user_agent', 'TEXT')])

# DROP TABLES

songplay_table_drop = songplays_properties.queries['drop_table']
user_table_drop = users_properties.queries['drop_table']
song_table_drop = songs_properties.queries['drop_table']
artist_table_drop = artists_properties.queries['drop_table']
time_table_drop = time_properties.queries['drop_table']

# CREATE TABLES

songplay_table_create = songplays_properties.queries['create_table']
user_table_create = users_properties.queries['create_table']
song_table_create = songs_properties.queries['create_table']
artist_table_create = artists_properties.queries['create_table']
time_table_create = time_properties.queries['create_table']

# INSERT RECORDS

songplay_table_insert = songplays_properties.queries['insert_into']
user_table_insert = users_properties.queries['insert_into']
song_table_insert = songs_properties.queries['insert_into']
artist_table_insert = artists_properties.queries['insert_into']
time_table_insert = time_properties.queries['insert_into']

# FIND SONGS

song_select = ("""
SELECT artists.artist_id, song_id
FROM songs
JOIN artists
  ON songs.artist_id = artists.artist_id
WHERE
    title = %s
    AND name = %s
    AND duration = %s;
""")

# QUERY LISTS

create_table_queries = [artist_table_create, user_table_create, song_table_create,
                        time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

if __name__ == '__main__':
    def print_queries():
        queries = list()
        queries.extend(create_table_queries)
        queries.extend(drop_table_queries)
        for query in queries:
            print(query)

    # print(songplays_properties.columns)

    postgres_table_properties = [users_properties, songs_properties, artists_properties,
                                 time_properties, songplays_properties]

    for p in postgres_table_properties:
        pass

    print(songplays_properties.queries['insert_into'])
