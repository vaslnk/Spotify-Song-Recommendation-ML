import requests
import json
import ijson

resp = requests.get('http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=ed%20sheeran&track=perfect&api_key=b7dfd0b8c572ef65aaf36c5f48bc1ee3&format=json')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
else:
    with open(resp.json(), 'r') as f:
        objects = ijson.items(f, 'meta.view.columns.item')
        columns = list(objects)
