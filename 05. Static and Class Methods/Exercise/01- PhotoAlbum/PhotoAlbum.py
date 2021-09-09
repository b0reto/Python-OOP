_PAGE_PHOTOS = 4
# _SUCCESS = f"{label} photo added successfully on page {pindex} slot "
_FAILED = "No more free slots"
_DASHES = f"{11 * '-'}\n"


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.pindex = 1
        self.slot = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // _PAGE_PHOTOS
        return cls(pages)

    def have_space(self) -> bool:
        return self.pindex < self.pages and len(self.photos[self.pindex]) < _PAGE_PHOTOS

    def new_page(self) -> int:
        if self.pindex > self.pages:
            return _FAILED
        if len(self.photos[self.pindex]) == _PAGE_PHOTOS:
            self.pindex += 1
            self.slot = 0
        return self.pindex

    def add_photo(self, label: str) -> str:
        NO_SPACE = False
        if not self.have_space():
            NO_SPACE = True
            self.new_page()

        if not NO_SPACE:
            self.photos[self.pindex].append(label)
        else:
            self.photos.append([])
            self.photos[self.pindex].append(label)
        self.slot += 1
        return f"{label} photo added successfully on page {self.pindex} slot {self.slot}"

    def display(self):
        res = ""
        res += _DASHES
        for el in self.photos:
            if not el:
                continue
            res += f"{len(el)*' []'}\n".lstrip()
            res += _DASHES


        return res.rstrip()
        # res = ""
        # for el in album.photos:
        #     res += f"{el}\n"
        #     res += _DASHES
        # return res


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
