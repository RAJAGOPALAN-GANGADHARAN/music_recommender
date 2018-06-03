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

    # makes prediction based on end user values
    n = coo.shape[1]
    try: scores = model.predict(user, np.arange(n))
    except ValueError:
        print('entered artists not found')
    
    # get top 10 recommendations
    top_scores = np.argsort(-scores)[:10]

    # determine top 5 recommendations
    top_recommendations = []
    for score in top_scores.tolist():
        if len(top_recommendations) == 5: break
        for artist_id, values in data['artists'].items():
            if int(score) == values['id']:
                if values['name'] == 'rock universal': break
                elif values['name'] == my_artists[0]: break
                elif values['name'] == my_artists[1]: break
                elif values['name'] == my_artists[2]: break
                else: 
                    top_recommendations.append(values['name'])
                    break
    
    # disply top 5 recommendations 
    print('Your music recommedations are:')
    for i in range(5):
        print(' - %s' % top_recommendations[i])

# get recommendations from model
get_recommendations(model, data['matrix'], data['users'])