"""
    iterates over the million playlist dataset and outputs info
    about what is in there.

    Usage:

        python stats.py path-to-mpd-data
"""
import sys
import json
import re
import collections
import os
import datetime

total_playlists = 0
total_tracks = 0
tracks = set()
artists = set()
albums = set()
titles = set()
total_descriptions = 0
ntitles = set()
title_histogram = collections.Counter()
artist_histogram = collections.Counter()
track_histogram = collections.Counter()
last_modified_histogram = collections.Counter()
num_edits_histogram = collections.Counter()
playlist_length_histogram = collections.Counter()
num_followers_histogram = collections.Counter()

quick = False
max_files_for_quick_processing = 5

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
    print "number of playlists with descriptions", total_descriptions
    print "number of unique normalized titles", len(ntitles)
    print "avg playlist length", float(total_tracks) / total_playlists
    print
    print "top playlist titles"
    for title, count in title_histogram.most_common(20):
        print "%7d %s" % (count, title)

    print
    print "top tracks"
    for track, count in track_histogram.most_common(20):
        print "%7d %s" % (count, track)

    print
    print "top artists"
    for artist, count in artist_histogram.most_common(20):
        print "%7d %s" % (count, artist)

    print
    print "numedits histogram"
    for num_edits, count in num_edits_histogram.most_common(20):
        print "%7d %d" % (count, num_edits)

    print
    print "last modified histogram"
    for ts, count in last_modified_histogram.most_common(20):
        print "%7d %s" % (count, to_date(ts))

    print
    print "playlist length histogram"
    for length, count in playlist_length_histogram.most_common(20):
        print "%7d %d" % (count, length)

    print
    print "num followers histogram"
    for followers, count in num_followers_histogram.most_common(20):
        print "%7d %d" % (count, followers)


def normalize_name(name):
    name = name.lower()
    name = re.sub(r"[.,\/#!$%\^\*;:{}=\_`~()@]", ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def to_date(epoch):
    return datetime.datetime.fromtimestamp(epoch).strftime("%Y-%m-%d")


def process_playlist(playlist):
    global total_playlists, total_tracks, total_descriptions

    total_playlists += 1
    # print playlist['playlist_id'], playlist['name']

    if 'description' in playlist:
        total_descriptions += 1

    titles.add(playlist['name'])
    nname = normalize_name(playlist['name'])
    ntitles.add(nname)
    title_histogram[nname] += 1

    playlist_length_histogram[playlist['num_tracks']] += 1
    last_modified_histogram[playlist['modified_at']] += 1
    num_edits_histogram[playlist['num_edits']] += 1
    num_followers_histogram[playlist['num_followers']] += 1

    for track in playlist['tracks']:
        total_tracks += 1
        albums.add(track['album_uri'])
        tracks.add(track['track_uri'])
        artists.add(track['artist_uri'])

        full_name = track['track_name'] + " by " + track['artist_name']
        artist_histogram[track['artist_name']] += 1
        track_histogram[full_name] += 1


def process_info(_):
    pass


if __name__ == '__main__':
    path = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == '--quick':
        quick = True
    process_mpd(path)
