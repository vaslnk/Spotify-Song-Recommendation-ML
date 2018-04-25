"""
    shows deep stats for the MPD

    usage:

        python deeper_stats.py path-to-mpd-data/
"""
import sys
import json
import re
import collections
import os

total_playlists = 0
total_tracks = 0
tracks = set()
artists = set()
albums = set()
titles = set()
ntitles = set()
full_title_histogram = collections.Counter()
title_histogram = collections.Counter()
artist_histogram = collections.Counter()
track_histogram = collections.Counter()

quick = False
max_files_for_quick_processing = 50


def process_mpd(path):
    count = 0
    filenames = os.listdir(path)
    for filename in sorted(filenames):
        if filename.startswith("mpd.slice.") and filename.endswith(".json"):
            fullpath = os.sep.join((path, filename))
            f = open(fullpath)
            js = f.read()
            f.close()
            mpd_slice = json.loads(js)
            process_info(mpd_slice['info'])
            for playlist in mpd_slice['playlists']:
                process_playlist(playlist)
            count += 1

            if quick and count > max_files_for_quick_processing:
                break

    show_summary()


def show_summary():
    print
    print "number of playlists", total_playlists
    print "number of tracks", total_tracks
    print "number of unique tracks", len(tracks)
    print "number of unique albums", len(albums)
    print "number of unique artists", len(artists)
    print "number of unique titles", len(titles)
    print "number of unique normalized titles", len(ntitles)
    print "avg playlist length", float(total_tracks) / total_playlists
    print
    print "full playlist titles"
    for title, count in full_title_histogram.most_common():
        print "%7d %s" % (count, title)
    print

    print "top playlist titles"
    for title, count in title_histogram.most_common():
        print "%7d %s" % (count, title)
    print

    print "top tracks"
    for track, count in track_histogram.most_common(10000):
        print "%7d %s" % (count, track)

    print
    print "top artists"
    for artist, count in artist_histogram.most_common(10000):
        print "%7d %s" % (count, artist)


def normalize_name(name):
    name = name.lower()
    name = re.sub(r"[.,\/#!$%\^\*;:{}=\_`~()@]", ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def process_playlist(playlist):
    global total_playlists, total_tracks

    total_playlists += 1
    # print playlist['playlist_id'], playlist['name']

    titles.add(playlist['name'])
    nname = normalize_name(playlist['name'])
    ntitles.add(nname)
    title_histogram[nname] += 1
    full_title_histogram[playlist['name'].lower()] += 1

    for track in playlist['tracks']:
        total_tracks += 1
        albums.add(track['album_uri'])
        tracks.add(track['track_uri'])
        artists.add(track['artist_uri'])

        full_name = track['track_name'] + " by " + track['artist_name']
        artist_histogram[track['artist_name']] += 1
        track_histogram[full_name] += 1


def process_info(info):
    for k, v in info.items():
        print "%-20s %s" % (k + ":", v)
    print


if __name__ == '__main__':
    quick = False
    path = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == '--quick':
        quick = True
    process_mpd(path)
