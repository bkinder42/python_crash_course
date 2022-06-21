def make_album(title, artist, num_songs=None):
    album = {'title': title, 'artist': artist}
    if num_songs:
        album['num_songs'] = num_songs
    return album

johnny = make_album("Gently Johnny My Jingalo", "Various Artists", 12)
dive = make_album("Side Pony", "Lake Street Dive", 12)
bonanza = make_album("Straker's Disco Sounds", "Straker")

print(johnny)
print(dive)
print(bonanza)