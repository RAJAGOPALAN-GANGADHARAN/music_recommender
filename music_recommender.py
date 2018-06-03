import numpy as np
from lightfm import LightFM
from get_lastfm import get_lastfm, my_artists
import sys

# get data matrix, artists, and users from get_lastfm
data = get_lastfm()

# apply model to data set
model = LightFM(loss='warp')
model.fit(data['matrix'], epochs=30, num_threads=2)

# get recommendations from model 
def get_recommendations(model, coo, user):

    # makes prediction based on end user values
    n = coo.shape[1]
    try: scores = model.predict(user, np.arange(n))
    except ValueError:
        print('entered artists not found')
        sys.exit()
    
    # get top 10 recommendations
    top_recommendations = []
    values = list(data['artists'].values())
    top_scores = np.argsort(-scores)[:10]
    for score in top_scores:
        recommendation = values[score]['name']
        if recommendation == 'rock universal': continue
        elif recommendation == my_artists[0]: continue
        elif recommendation == my_artists[1]: continue
        elif recommendation == my_artists[2]: continue
        else: top_recommendations.append(recommendation)
    
    # disply top 5 recommendations 
    print('Your music recommedations are:')
    for i in range(5):
        print(' - %s' % top_recommendations[i])

# get recommendations from model
get_recommendations(model, data['matrix'], data['users'])
