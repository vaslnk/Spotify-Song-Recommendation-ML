
"""
    pretty printer for the MPD

    Usage:
        python show.py - show all the playlists in the MPD
        python show.py 1008 1120 4356 - show the playlists with the given pids
        python show.py 1000-1020 1989 99870-99999 - show the playlists in the given range

"""


import sys
import json
import codecs
import datetime


pretty = True
compact = False
cache = {}

def print_playlist(playlist):
    if pretty:
        print '===', playlist['pid'], '==='
        print playlist['name']
        print "  followers", playlist['num_followers']
        print "  modified", datetime.datetime.fromtimestamp(playlist['modified_at']).strftime("%Y-%m-%d")
        print "  edits", playlist['num_edits']
        print
        if not compact:
            for track in playlist['tracks']:
                print "%3d %s - %s" %(track['pos'], track['track_name'], track['album_name'])
            print
    else:
        print json.dumps(playlist, indent=4)


def show_playlist(pid):
    if pid >=0 and pid < 1000000:
        low = 1000 * int(pid / 1000)
        high = low + 999
        offset = pid - low
        path = "data/mpd.slice." + str(low) + '-' + str(high) + ".json"
        if not path in cache:
            f = codecs.open(path, 'r', 'utf-8')
            js = f.read()
            f.close()
            playlist = json.loads(js)
            cache[path] = playlist

        playlist = cache[path]['playlists'][offset]
        print_playlist(playlist)


def show_playlists_in_range(start, end):
    try:
        istart = int(start)
        iend = int(end)
        if istart <= iend and istart >= 0 and iend <= 1000000:
            for pid in xrange(istart, iend):
                show_playlist(pid)
    except:
        raise
        print "bad pid"
    

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if arg == '--pretty':
            pretty = True
        elif arg == '--compact':
            compact = True
        elif arg == '--raw':
            pretty = False
        elif '-' in arg:
            fields = arg.split('-')
            if len(fields) == 2:
                start = fields[0]
                end = fields[1]
                show_playlists_in_range(start, end)
        else:
            pid = int(arg)
            show_playlist(pid)
