import urllib.parse

from flask import Flask, render_template, request, send_file, redirect
from filesystem_utils import localList, get_thumbnail, webstyle_path, machinestyle_path, delete_path
import os

LWWFM = Flask('Lightweight web file manager')

BASE_PATH = 'files'

current_path = '/'

@LWWFM.route('/', methods = ['GET', 'POST'])
def index():
    '''
    viewmode = 'thumbnails'
    if 'viewmode' in request.args:
        if request.args.get('viewmode') == 'thumbnails':
            viewmode = 'thumbnails'
        elif request.args.get('viewmode') == 'list':
            viewmode = 'list'
    filelist = localList(BASE_PATH)
    '''
    if request.method == 'GET':
        filelist = localList(BASE_PATH)
        viewmode = 'thumbnails'
        if 'viewmode' in request.args:
            if request.args.get('viewmode') == 'thumbnails':
                viewmode = 'thumbnails'
            elif request.args.get('viewmode') == 'list':
                viewmode = 'list'

        return render_template('index.html',
                                viewmode = viewmode,
                                itemlist = filelist,
                                current_path = current_path)

    if request.method == 'POST':
        f = request.files['file']
        file_path = os.path.join(BASE_PATH, f.filename)
        print(file_path)
        f.save(file_path)
        return redirect(current_path)




@LWWFM.route('/files/<path:path>', methods = ['GET', 'POST'])
def action(path):
    current_path = webstyle_path(os.path.join(os.sep, BASE_PATH, path))
    if request.method == 'GET':
        path = urllib.parse.unquote(path).split('/')
        path = os.path.join(BASE_PATH, *path)
        viewmode = 'thumbnails'
        if 'viewmode' in request.args:
            if request.args.get('viewmode') == 'thumbnails':
                viewmode = 'thumbnails'
            elif request.args.get('viewmode') == 'list':
                viewmode = 'list'
        #viewmode = 'thumbnails' if not ('viewmode' in request.args) or request.args
        if os.path.isdir(path):
            filelist = localList(path)
            return render_template('index.html',
                                   viewmode=viewmode,
                                   itemlist=filelist,
                                   current_path=current_path)
        else:
            #print(path)
            return send_file(path)

    if request.method == 'POST':
        f = request.files['file']
        file_path = os.path.join(machinestyle_path(current_path).lstrip(os.sep), f.filename)
        f.save(file_path)
        return redirect(current_path)

    if request.method == 'DELETE':
        print('del')
        return redirect(current_path)


@LWWFM.route('/delete/<path:path>', methods = ['POST'])
def delete(path):
    current_path = webstyle_path(os.path.join(os.sep, path))
    delete_path(path)
    print('del ', current_path)
    print(request.args)
    redirect_url = os.path.dirname(current_path)
    print(redirect_url)
    return redirect(redirect_url)


if __name__ == '__main__':
    #print(get_thumbnail('files\Screenshot from 2022-09-27 14-27-54.png'))
    LWWFM.run('0.0.0.0')


