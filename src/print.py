"""
    pretty prints the MPD

    usage:
        python print.py path-mpd/
"""
import sys
import json
import time
import os


def process_playlists(path):
    filenames = os.listdir(path)
    for filename in sorted(filenames):
        if filename.startswith("mpd.slice.") and filename.endswith(".json"):
            fullpath = os.sep.join((path, filename))
            f = open(fullpath)
            js = f.read()
            f.close()
            mpd_slice = json.loads(js)
            for playlist in mpd_slice['playlists']:
                print_playlist(playlist)


def print_playlist(playlist):
    print "=====", playlist['pid'], '===='
    print "name:          ", playlist['name']
    ts = time.strftime('%Y-%m-%d %H:%M:%S',
                       time.localtime(playlist['modified_at'] / 1000))

    print "last_modified: ", ts
    print "num edits: ", playlist['num_edits']
    print "num followers: ", playlist['num_followers']
    print "num artists: ", playlist['num_artists']
    print "num albums: ", playlist['num_albums']
    print "num tracks: ", playlist['num_tracks']
    print
    for i, track in enumerate(playlist['tracks']):
        print "   %3d %s - %s - %s" % (i + 1, track['track_name'],
                                       track['album_name'],
                                       track['artist_name'])
    print


if __name__ == '__main__':
    path = sys.argv[1]
    process_playlists(path)
