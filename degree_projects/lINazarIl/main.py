import urllib.parse, os
from flask import Flask, render_template, request, send_file, redirect, url_for
from filesystem_utils import localList, get_thumbnail, webstyle_path, machinestyle_path, delete_path, create_dir


LWWFM = Flask('Lightweight web file manager')
BASE_PATH = 'files'


@LWWFM.route('/', methods = ['GET', 'POST'])
@LWWFM.route('/files', methods=['GET', 'POST'])
def index():
    viewmode = 'thumbnails'
    if 'viewmode' in request.args and viewmode in ['thumbnails', 'list']:
        viewmode = request.args['viewmode']

    if request.method == 'GET':
        current_path = webstyle_path(os.path.join(os.sep, BASE_PATH))
        path_for_view = current_path
        filelist = localList(BASE_PATH)

        return render_template('index.html',
                                viewmode = viewmode,
                                itemlist = filelist,
                                current_path = '/',
                                path_for_view = path_for_view)

    if request.method == 'POST':
        f = request.files['file']
        file_path = os.path.join(BASE_PATH, f.filename)
        print(file_path)
        f.save(file_path)
        return redirect(BASE_PATH+f'?viewmode={ viewmode }')


@LWWFM.route('/files/<path:path>', methods = ['GET', 'POST'])
def action(path):
    viewmode = 'thumbnails'
    if 'viewmode' in request.args and viewmode in ['thumbnails', 'list']:
        viewmode = request.args['viewmode']
    current_path = webstyle_path(os.path.join(os.sep, BASE_PATH, path))
    path_for_view = current_path
    current_path = urllib.parse.quote(current_path)
    if request.method == 'GET':
        path = urllib.parse.unquote(path).split('/')
        path = os.path.join(BASE_PATH, *path)
        #viewmode = 'thumbnails' if not ('viewmode' in request.args) or request.args
        if os.path.isdir(path):
            filelist = localList(path)
            return render_template('index.html',
                                   viewmode = viewmode,
                                   itemlist = filelist,
                                   current_path = current_path,
                                   path_for_view = path_for_view)
        else:
            return send_file(path)

    if request.method == 'POST':
        if 'file' in request.files:
            f = request.files['file']
            file_path = os.path.join(BASE_PATH, machinestyle_path(path).lstrip(os.sep), f.filename)
            f.save(file_path)
        return redirect(current_path+f'?viewmode={ viewmode }')


@LWWFM.route('/delete/<path:path>', methods = ['POST'])
def delete(path):
    viewmode = 'thumbnails'
    if 'viewmode' in request.args and viewmode in ['thumbnails', 'list']:
        viewmode = request.args['viewmode']

    current_path = webstyle_path(os.path.join(os.sep, path))
    delete_path(path)
    redirect_url = os.path.dirname(current_path)+f'?viewmode={ viewmode }'
    return redirect(redirect_url)


@LWWFM.route('/create/', methods = ['POST'])
@LWWFM.route('/create/<path:path>', methods = ['POST'])
def create(path='files'):
    viewmode = 'thumbnails'
    if 'viewmode' in request.args and viewmode in ['thumbnails', 'list']:
        viewmode = request.args['viewmode']

    current_path = webstyle_path(os.path.join(os.sep, path))
    if 'dirname' in request.form:
        create_dir(path, request.form['dirname'])
    else:
        create_dir(path, None)
    return redirect(current_path+f'?viewmode={ viewmode }')

if __name__ == '__main__':
    #print(get_thumbnail('files\Screenshot from 2022-09-27 14-27-54.png'))
    LWWFM.run('0.0.0.0')


