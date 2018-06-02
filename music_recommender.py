import numpy as np
from lightfm import LightFM
from get_lastfm import get_lastfm, my_artist, my_artist2, my_artist3

# get final data set from get_lastfm
data = get_lastfm()

model = LightFM(loss='warp')
model.fit(data['matrix'], epochs=30, num_threads=2)

def get_recommendations(model, coo, my_user):

    n = coo.shape[1]

    try: scores = model.predict(my_user, np.arange(n))
    except ValueError:
        print('entered artists not found')
    top_scores = np.argsort(-scores)[:10]

    print('Your music recommedations are:')

    for score in top_scores.tolist():
        for artist_id, values in data['artists'].items():
            if int(score) == values['id']:
                if values['name'] == 'rock universal': continue
                if values['name'] == my_artist or values['name'] == my_artist2 or values['name'] == my_artist3: continue
                print(' - %s' % values['name'])

get_recommendations(model, data['matrix'], data['users'])