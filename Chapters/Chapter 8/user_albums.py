def make_album(title, artist, num_songs=None):
    album = {'title': title, 'artist': artist}
    if num_songs:
        album['num_songs'] = num_songs
    return album

while True:
    print("(Enter q at any time to quit)\n\n")
    artist = input("Please enter the artist: ")
    if artist == 'q':
        break
    title = input ("Please enter the album title: ")
    if title == 'q':
        break
    num_songs = input("Please enter the number of songs (or leave blank "
        "for unknown): ")
    if num_songs:
        if num_songs == 'q':
            break
        else:
            num_songs = int(num_songs)
            album = make_album(title, artist, num_songs)
    else:
        album = make_album(title, artist)
    print(f"{album}\n\n")