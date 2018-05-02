


# Spotify Million Playlists Dataset (RecSys 2018) Challenge Submission 
by Jack Vasylenko, Chitwan Kaudan, Anith Patel, Tyler Larsen, William Wang

Place the 'data' folder obtained using Spotify's official [dataset](recsys-challenge.spotify.com/dataset) into the root folder of the project and run the following command:
```
python restructureData.py 
```



## About the dataset:
The MPD contains a million user-generated playlists. These playlists
were created during the period of January 2010 through October 2017.
Each playlist in the MPD contains a playlist title, the track list
(including track metadata) editing information (last edit time, 
number of playlist edits) and other miscellaneous information 
about the playlist. See the **Detailed
Description** section for more details.


### License
Usage of the Million Playlist Dataset is subject to these 
[license terms](https://recsys-challenge.spotify.com/license)

### Citing the Million Playlist Dataset

Citation information for the dataset can be found at
[recsys-challenge.spotify.com/dataset](https://recsys-challenge.spotify.com/dataset)


### Getting the dataset
The dataset is available at [recsys-challenge.spotify.com/dataset](https://recsys-challenge.spotify.com/dataset)



### How was the dataset built
The Million Playist Dataset is created by sampling playlists from the billions of playlists that Spotify users have created over the years.  Playlists that meet the following criteria are selected at random:

 * Created by a user that resides in the United States and is at least 13 years old
 * Was a public playlist at the time the MPD was generated
 * Contains at least 5 tracks
 * Contains no more than 250 tracks
 * Contains at least 3 unique artists
 * Contains at least 2 unique albums
 * Has no local tracks (local tracks are non-Spotify tracks that a user has on their local device)
 * Has at least one follower (not including the creator)
 * Was created after January 1, 2010 and before December 1, 2017
 * Does not have an offensive title
 * Does not have an adult-oriented title if the playlist was created by a user under 18 years of age

Additionally, some playlists have been modified as follows:

 * Potentially offensive playlist descriptions are removed
 * Tracks added on or after November 1, 2017 are removed

Playlists are sampled randomly, for the most part, but with some dithering to disguise the true distribution of playlists within Spotify. [Paper tracks](https://en.wikipedia.org/wiki/Fictitious_entry) may be added to some playlists to help us identify improper/unlicensed use of the dataset.
