# Define a class named Album to represent music albums
class Album:

    # Constructor method to initialize the Album object with name, number of songs, and artist
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name          # Album title
        self.number_of_songs = number_of_songs  # Number of songs in the album
        self.album_artist = album_artist      # Name of the artist

    # Method to return a readable string representation of the Album object
    def __str__(self):
        return f"album name: {self.album_name}\n\
album artist: {self.album_artist} \nnumber of songs: {self.number_of_songs}\n"

# Create a list of Album objects with sample data
albums1 = [
    Album('In Abandance', 12, 'Playboi Carti'),
    Album('Playboi Carti', 15, 'Playboi Carti'),
    Album('Die Lit', 19, 'Playboi Carti'),
    Album('Whole Lotta Red', 24, 'Playboi Carti'),
    Album('Music', 30, 'Playboi Carti')
]

# Print all albums in albums1
print("List of Albums:\n")
for album in albums1:
    print(album)  # Calls the __str__ method of Album to display details

# Sort albums1 list by the number of songs in each album (ascending order)
albums1.sort(key=lambda album: album.number_of_songs)

# Swap the first two albums in the sorted list (custom reordering)
albums1[0], albums1[1] = albums1[1], albums1[0]

# Create a copy of albums1 to make a new list albums2
albums2 = albums1[:]

# Add additional albums to albums2
albums2.append(Album('Dark Side of the Moon', 9, 'Pink Floyd'))
albums2.append(Album("Oops!... I Did It Again", 16, 'Britney Spears'))

# Sort albums2 alphabetically by album name
albums2.sort(key=lambda album: album.album_name)

# Prompt the user to search for an album by name
search_name = input("Please enter the album your searching for: ")

# Search for the album in albums2 (case-insensitive)
for index, album in enumerate(albums2):
    if album.album_name.lower() == search_name.lower():
        print(f"\n{search_name.title()} found at index: {index}")  # Album found
        break
else:
    # Executed if the album is not found in the list
    print(f"\n{search_name.title()} is not in list.")
