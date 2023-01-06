def make_album(artist_name, album_title, number_song=None):

    album = {
        'artist': artist_name,
        'title': album_title
    }

    if number_song:
        album['number_song'] = number_song

    return album

while True:
    print('INSERT YOUR ALBUM: ')
    print("(Enter 'q' at any time quit)")

    artist = input('Insert astist: ')
    if artist == 'q':
        break

    title = input('Insert album: ')
    if title == 'q':
        break

    all_album = make_album(artist, title, number_song=1)
    print(f'Your Album is {all_album}')

