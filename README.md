


# Spotify Million Playlists (RecSys 2018) Challenge Submission 
UC Berkeley Team: Jack Vasylenko, Chitwan Kaudan, Anith Patel, Tyler Larsen and William Wang.

# Databricks Spark Demo video: https://youtu.be/CQqzHpn5zE8

This project is a song recommendation system implemented using Spark MLib Alternating Squares Collaborative Filtering Algorithm trained on 1 million playlists open-sourced by Spotify.

<img src="https://upload.wikimedia.org/wikipedia/commons/2/26/Spotify_logo_with_text.svg" width="200">     <img src="https://venturebeat.com/wp-content/uploads/2017/06/databricks_logor_stacked_rgb_1200px.png" width="200">     <img src="https://spark.apache.org/images/spark-logo-trademark.png" width="200">     <img src="https://cdn-images-1.medium.com/max/1600/1*AD9ZSLXKAhZ-_WomszsmPg.png" width="200">


### About the dataset:
The MPD contains a million user-generated playlists. These playlists
were created during the period of January 2010 through October 2017.
Each playlist in the MPD contains a playlist title, the track list
(including track metadata) editing information (last edit time, 
number of playlist edits) and other miscellaneous information 
about the playlist.

## Obtaining The Data
Proceed with these steps to download Spotify's dataset (33 Gb) and convert the data into a memory-efficient format (~ 5 Gb) for use on the Databricks platform:
1. Download Spotify's official [dataset](recsys-challenge.spotify.com/dataset) and place the 'data' folder into the root folder of the project. 
2. Run the following command:
```
python restructureData.py 
```
This script populates the \data_csv folder with the data that can be used to create a Databricks table.

## 1. Exploratory data analysis:
```
EDA.ipynb
```
## 2. Using Neural Collaborative Filtering approach on a subset of data:
```
Neural-Collaborative-Filtering.ipynb
```

## 3. Training & Using Spark MLib Alternative Least Squares algorithm on all of data:
```
Spark-MLib-ALS.ipynb
```

### License
Usage of the Million Playlist Dataset is subject to these 
[license terms](https://recsys-challenge.spotify.com/license)
