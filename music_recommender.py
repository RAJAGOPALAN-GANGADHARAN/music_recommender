import numpy as np
from lightfm import LightFM
from get_lastfm import get_lastfm, my_artists

# get data matrix, artists, and users from get_lastfm
data = get_lastfm()

# apply model to data set
model = LightFM(loss='warp')
model.fit(data['matrix'], epochs=30, num_threads=2)

# get recommendations from model 
def get_recommendations(model, coo, user):

    n = coo.shape[1]

    try: scores = model.predict(user, np.arange(n))
    except ValueError:
        print('entered artists not found')
    top_scores = np.argsort(-scores)[:10]

    print('Your music recommedations are:')

    for score in top_scores.tolist():
        for artist_id, values in data['artists'].items():
            if int(score) == values['id']:
                if values['name'] == 'rock universal': continue
                for artist in my_artists:
                    if values['name'] == artist: continue
                print(' - %s' % values['name'])

get_recommendations(model, data['matrix'], data['users'])