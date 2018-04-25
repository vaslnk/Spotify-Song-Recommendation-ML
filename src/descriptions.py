
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

quick = False
max_files_for_quick_processing = 5
descriptions  = collections.Counter()
ndescriptions  = collections.Counter()

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
    print "descriptions"
    for k,v in descriptions.most_common():
        print v, k

    print 
    print "normalized descriptions"
    for k,v in ndescriptions.most_common():
        print v, k

def normalize_name(name):
    name = name.lower()
    name = re.sub(r"[.,\/#!$%\^\*;:{}=\_`~()@]", ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def process_playlist(playlist):
    if 'description' in playlist:
        desc = playlist['description']
        ndesc = normalize_name(desc)
        descriptions[desc] += 1
        ndescriptions[ndesc] += 1

def process_info(_):
    pass

if __name__ == '__main__':
    path = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == '--quick':
        quick = True
    process_mpd(path)
