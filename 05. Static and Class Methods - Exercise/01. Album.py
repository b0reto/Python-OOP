class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4


    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []


    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(PhotoAlbum)

