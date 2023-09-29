import os, hashlib, urllib, re, time, math, shutil
from PIL import Image

THUMBNAIL_PATH = os.path.join('static', 'thumbnails')
THUMBNAIL_SIZE = (200,200)

FILETYPHES = {
    'Video' :
        ['.mp4', '.3gp', '.webm', '.mkv'],
    'Sound' :
        ['.mp3', '.flac', '.opus'],
    'Images' :
        ['.jpg', '.jpeg', '.png', '.gif'],
    'Text' :
        ['.txt', '.json', '.html', '.css', '.js']
}

def human_readable_size(size):
    pass


def webstyle_path(path):
    path_in_list = re.split('\\\|/', path)
    web_path = '/'.join(path_in_list)
    return web_path

def machinestyle_path(path):
    path_in_list = re.split('\\\|/', path)
    return os.sep.join(path_in_list)

def sizeof_fmt(num, suffix='B'):
    magnitude = int(math.floor(math.log(num, 1024)))
    val = num / math.pow(1024, magnitude)
    if magnitude > 7:
        return '{:.1f}{}{}'.format(val, 'Yi', suffix)
    return '{:3.1f}{}{}'.format(val, ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi'][magnitude], suffix)

def localList(path):
    layer = []
    for i in os.listdir(path):
        item_path = os.path.join(path, i)
        web_path = webstyle_path(item_path)

        if os.path.isdir(os.path.join(path, i)):
            layer.append({'name': i,
                          'type': 'dir',
                          'thumbnail': get_thumbnail(path),
                          'path': urllib.parse.quote(web_path)
                          })
        elif os.path.isfile(os.path.join(path, i)):
            filestat = os.stat(os.path.join(path, i))
            file = {
                'name': i,
                'type': 'file',
                'filesize': sizeof_fmt(filestat.st_size),
                'mtime': time.strftime("%d.%m.%Y %H:%M", time.localtime(filestat.st_mtime)),
                'thumbnail': get_thumbnail(os.path.join(path, i)),
                'path': urllib.parse.quote(web_path)
            }
            layer.append(file)
    return layer

#this function returns path to thumbnail
def get_thumbnail(path):
    if os.path.isdir(path):
        image = Image.open(os.path.join('static', 'pics', 'directory_thumbnail.png'))
        image.thumbnail(THUMBNAIL_SIZE)
        image = image.convert('RGB')
        thumbnail_name = '.'.join(['directory_thumbnail',
                                   'thumbnail',
                                   'jpg'])
        image.save(os.path.join(THUMBNAIL_PATH, thumbnail_name))
        #return os.path.join(THUMBNAIL_PATH, thumbnail_name)
        return os.path.join('static', 'pics', 'directory_thumbnail.png')

    #calc hash for fast check files
    with open(path, 'rb') as f:
        hash = hashlib.md5()
        while dataBlock := f.read(512):
            hash.update(dataBlock)
        hash.update(f.read())
    hash = hash.hexdigest()

    filename = os.path.split(path)[1]
    fileextension = os.path.splitext(filename)[1]


    if fileextension in FILETYPHES['Video']:
        thumbnail_name = '.'.join([hash,
                                   'thumbnail',
                                   'jpg'])

        if thumbnail_name in os.listdir(THUMBNAIL_PATH):
           return os.path.join(THUMBNAIL_PATH, thumbnail_name)

        size_in_string = ':'.join(map(str, THUMBNAIL_SIZE))
        cmd = f'ffmpeg -i "{path}" ' \
              f'-ss 00:00:01.000 ' \
              f'-vframes 1 ' \
              f'-vf "scale={size_in_string}:force_original_aspect_ratio=decrease" ' \
              f'{os.path.join(THUMBNAIL_PATH, thumbnail_name)}'
        os.system(cmd)

        return os.path.join(THUMBNAIL_PATH, thumbnail_name)

    if fileextension in FILETYPHES['Text']:
        return os.path.join('static', 'pics', 'text_thumbnail.jpg')

    if fileextension in FILETYPHES['Sound']:
        return os.path.join('static', 'pics', 'music_thumbnail.png')

    #create thumbnail if type of item is image
    if fileextension in FILETYPHES['Images']:
        thumbnail_name = '.'.join([hash,
                                   'thumbnail',
                                   'jpg'])

        #return previous generated thumbnail if exists
        if thumbnail_name in os.listdir(THUMBNAIL_PATH):
           return os.path.join(THUMBNAIL_PATH, thumbnail_name)

        #else generate thumbnail
        try:
            image = Image.open(path)
            image.thumbnail(THUMBNAIL_SIZE)
            image = image.convert('RGB')
            image.save(os.path.join(THUMBNAIL_PATH, thumbnail_name))
            return os.path.join(THUMBNAIL_PATH, thumbnail_name)
        except IOError:
            pass

    if fileextension == '.pdf':
        return os.path.join('static', 'pics', 'pdf_thumbnail.png')

    return os.path.join('static', 'pics', 'file_thumbnail.png')

def delete_path(path):
    path = path.lstrip('/')
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.remove(path)

def create_dir(path, dirname):
    if dirname:
        try:
            os.makedirs(os.path.join(path, dirname), exist_ok = True)
        except:
            pass