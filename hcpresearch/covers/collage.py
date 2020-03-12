import random
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import urllib.request
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
import os

url = "http://covers.openlibrary.org/b/isbn/"


def download_file(url):
    no = random.randint(1, 1000)
    try:
        os.makedirs("../static/covers")
    except FileExistsError:
        # directory already exists
        pass

    path = '../static/covers/newfile-' + str(no) + '.jpg'
    urllib.request.urlretrieve(url, path)
    return path


def create_collage(cells, cols=3, rows=3):
    print(len(cells))
    w, h = Image.open(cells[0]['path']).size
    collage_width = cols * w
    collage_height = rows * h
    new_image = Image.new('RGB', (collage_width, collage_height))
    cursor = (0, 0)
    for cell in cells:
        # place image
        new_image.paste(Image.open(cell['path']), cursor)

        # move cursor
        y = cursor[1]
        x = cursor[0] + w
        if cursor[0] >= (collage_width - w):
            y = cursor[1] + h
            x = 0
        cursor = (x, y)

    tempfile_io = BytesIO()
    new_image.save(tempfile_io, format='JPEG')
    image_file = ContentFile(tempfile_io.getvalue())
    no = random.randint(1, 1000)
    filename = 'collapse-' + str(no) + '.jpg'
    img = InMemoryUploadedFile(image_file, None, filename, 'image/jpeg', image_file.tell, None)
    return img


# create_collage(image_info, cols=3, rows=3)


def createIBNS(ibns):
    image_info = []
    for cover in ibns:
        url_ibn = url + cover + '-L.jpg'
        path = download_file(url_ibn)
        spot_info = {
            'name': cover,
            'path': path
        }
        image_info.append(spot_info)
    return image_info
