
import os
import sys
import json


def jsonrename(item):
    data = json.load(open(item.path, 'r'))
    if 'title' not in data:
        return # assuming album metadata or similar
    expectedname = data['title']+'.json'
    if item.name != expectedname:
        newname = item.path[:-len(item.name)]+expectedname
        os.rename(item.path, newname)
        print('Renamed', item.path, 'to', newname)

def jsonrenamedir(dirname):
    for item in os.scandir(dirname):
        if item.is_file():
            if item.name.split('.')[-1] == 'json':
                jsonrename(item)
        else: # recurse
            jsonrenamedir(item.path)

def jsonlower(item):
    if len(item.name.split('.')) >= 3:
        preext = '.'.join(item.name.split('.')[:-2])
        subext = item.name.split('.')[-2]
        if not subext.islower():
            newpath = item.path[:-len(item.name)] + preext+'.'+subext.lower()+'.json'
            os.rename(item.path, newpath)
            print('Renamed', item.path, 'to', newpath)

        if subext.lower() == 'jpeg':
            newpath = item.path[:-len(item.name)] + preext+'.jpg.json'
            os.rename(item.path, newpath)
            print('Renamed', item.path, 'to', newpath)

def jsonlowerdir(dirname):
    for item in os.scandir(dirname):
        if item.is_file():
            if item.name.split('.')[-1] == 'json':
                jsonlower(item)
        else: # recurse
            jsonlowerdir(item.path)

def medialowerdir(dirname):
    for item in os.scandir(dirname):
        if item.is_file():
            if item.name.split('.')[-1] != 'json':
                medialower(item)
        else: # recurse
            medialowerdir(item.path)

def medialower(item):
    ext = item.name.split('.')[-1]
    if not ext.islower():
        newpath = item.path[:-len(ext)] + ext.lower()
        os.rename(item.path, newpath)
        print('Renamed', item.path, 'to', newpath)

    if ext.lower() == 'jpeg':
        newpath = item.path[:-len(ext)] + 'jpg'
        os.rename(item.path, newpath)
        print('Renamed', item.path, 'to', newpath)


if __name__ == '__main__':
    maindir = sys.argv[1]
    
    print('Fixing json filenames ====')
    jsonrenamedir(maindir)

    print('Lowering json filenames ====')
    jsonlowerdir(maindir)

    print('Lowering media filenames ====')
    medialowerdir(maindir)

    print('Done.')

