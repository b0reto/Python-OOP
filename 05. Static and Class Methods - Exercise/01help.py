pages = int(input())
photos = []
MAX_PHOTOS_PER_PAGE = 4
photos_COUNT = int(input())
c = 0
while photos_COUNT > 0:
    for row in range(pages):
        for col in range(MAX_PHOTOS_PER_PAGE):
            photos.append([row, col])
            photos_COUNT -= 1

print(photos)
