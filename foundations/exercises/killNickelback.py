# Define a set that contains tuples. Each tuple should contain two strings:
# 1. The name of an artist
# 2. A song by that artist
# Make sure that some of the songs are from the band Nickelback. You can see a list of their greatest hits on Amazon.

songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('Eminem', 'Curtain Call'),
    ('Nickelback', 'Rockstar'),
    ('Vanilla Ice', 'Ice Ice Baby')
};

# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.
songs_wo_nickelback = {each[0] + ' : ' + each[1] for each in songs if each[0] != 'Nickelback'};
print(songs_wo_nickelback);

only_nickelback = {each[0] + ' : ' + each[1] for each in songs if each[0] == 'Nickelback'};
print(only_nickelback);
