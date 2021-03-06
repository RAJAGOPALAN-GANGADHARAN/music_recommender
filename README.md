# music_recommender
A music recommendation system using the Last.fm API and the LightFM library. 

## Dependencies

1. lightfm 
2. scipy
3. numpy

Run the below command in terminal:

```
pip3 install -r requirements.txt
```

## Usage

Download the dataset file [here](http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/lastfm-360K.html). Move the dataset file to the music_recommender directory. The presumed file path is:

```
/music_recommender/lastfm-dataset-360K.tar.gz
```

Run the below script in terminal:

```
python3 music_recommender.py
```

Enter your top 3 favorite artists before March 2010 (lowercase). Displays artists that are found in recommendation system. Result is top 10 artist recommendations. 
