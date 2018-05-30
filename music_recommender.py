import numpy as np
from lightfm import LightFM
from get_lastfm import get_lastfm

# get final data set from get_lastfm
data = get_lastfm()

model = LightFM(loss='warp')
model.fit(data['matrix'], epochs=30, num_threads=2)

def get_recommendations(model, coo, users):

    n = coo.shape[1]

    for user in users:
        scores = model.predict(user, np.arange(n))
        top_scores = np.argsort(-scores)[:3]

        print('Recomendations for user %s:' % user)

        for score in top_scores.tolist():
            for artist_id, values in data['artists'].items():
                if int(score) == values['id']:
                    print('   - %s' % values['name'])

user_1 = input('Select user 1 (0 to %s): ' % data['users'])
user_2 = input('Select user 2 (0 to %s): ' % data['users'])
user_3 = input('Select user 3 (0 to %s): ' % data['users'])

get_recommendations(model, data['matrix'], [user_1, user_2, user_3])