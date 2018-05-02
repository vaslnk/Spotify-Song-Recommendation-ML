#!/usr/bin/env python

import pandas as pd
import numpy as np
import json

def jsonToCSV():
    start = 0
    end = 1000
    while end != 6000:
        songPlaylistArray = []
        path = 'data/mpd.slice.' + str(start) + "-" + str(end-1) + '.json'
        d = json.load(open(path, 'r'))
        thisSlice = pd.DataFrame.from_dict(d['playlists'], orient='columns')
        for index, row in thisSlice.iterrows():
            for track in row['tracks']:
                songPlaylistArray.append([track['track_uri'], track['artist_name'], track['track_name'], row['pid']])
        songPlaylist = pd.DataFrame(songPlaylistArray, columns=['trackid', 'artist_name', 'track_name', 'pid'])
        songPlaylist.to_csv('data_CSV/' + str(start) + "-" + str(end-1) + '.csv', index=False)
        start += 1000
        end += 1000


if __name__ == '__main__':
    jsonToCSV()
