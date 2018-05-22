import numpy as np
from lightfm import LightFM
from get_lastfm import get_lastfm


data = get_lastfm()

model = LightFM(loss='warp')
model.fit(data['matrix'], epochs=30, num_threads=2)

def get_recommendations(model, coo_mtrx, users_ids):

    n_items = coo_mtrx.shape[1]

    for user in users_ids:
        scores = model.predict(user, np.arange(n_items))
        top_scores = np.argsort(-scores)[:3]

        print('Recomendations for user %s:' % user)

        for x in top_scores.tolist():
            for artist, values in data['artists'].items():
                if int(x) == values['id']:
                    print('   - %s' % values['name'])

        print('\n') 


user_1 = input('Select user_1 (0 to %s): ' % data['users'])
user_2 = input('Select user_2 (0 to %s): ' % data['users'])
user_3 = input('Select user_3 (0 to %s): ' % data['users'])
print('\n') 

get_recommendations(model, data['matrix'], [user_1, user_2, user_3])