def make_shirt(size = "LARGE Men's", message = 'I love Python by default!'):
    print("\nThe size of the shirt is " + size + ".")
    print("The message on the shirt will be: '" + message + "'.")

def city_country(city, country):
    pair = city.title() + ", " + country.title()
    return pair

sz = 'XL'
ms = 'I love Python!'
make_shirt(sz, ms)

make_shirt()

make_shirt(size = 'L', message = 'I love Python a lot!')

location = city_country("Santiago", "Chile")
print("\nYour location is " + location)

def make_album(artist, title, tracks=''):
    album = {'artist_name': artist,
    'album_title': title}
    if tracks:
        album['num_tracks'] = tracks
    return album

album = make_album('David Bowie', 'Scary Monsters')
print("\n")
print(album)
album = make_album('Paul Weller', 'Wildwood')
print("\n")
print(album)
album = make_album('Radiohead', 'Okay, Computer')
print("\n")
print(album)
print("\n")

albums = []
album = make_album('David Bowie', 'Lodger', 10)
albums.append(album)
album = make_album('Paul Weller', 'Stanley Road', 8)
albums.append(album)
album = make_album('Radiohead', 'The Bends', 6)
albums.append(album)

for album in albums:
    #print("\n")
    print(album)

print("Type quit to exit album data entry loop.")
prompt1 = "\nPlease enter the name of the album's artist: "
prompt2 = "\nPlease enter the name of the album: "
prompt3 = "\n(Optional). Please enter the number of tracks: "

while True:
    artist_name = input(prompt1)

    if artist_name == 'quit':
        print("Thank you for playing!")
        break

    album_name = input(prompt2)
    num_tracks = input(prompt3)

    album = make_album(artist_name, album_name, num_tracks)
    print("\n")
    print(album)
