from project.album import Album
from project.song import Song


class Band:
    albums = []

    def __init__(self, name):
        self.name = name

    def add_album(self, album: Album):
        if album in Band.albums:
            return f"Band {self.name} already has {album.name} in their library."

        Band.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for album1 in self.albums:
            if album1.name == album_name:
                if album1.published:
                    return "Album has been published. It cannot be removed."
                else:
                    return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        separator = "\n"
        return f"Band {self.name}\n" \
               f"{separator.join(f'{album.details()}' for album in self.albums)}"


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initiall D"))
print(band.details())







