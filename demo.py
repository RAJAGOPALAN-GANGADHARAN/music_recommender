import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
import sys

#fetch data and format it
data = fetch_movielens(min_rating=4.0)

#create model
model = LightFM(loss='warp')

#train model
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):

    #number of users and movies in training data
    n_users, n_items = data['train'].shape

    #generate recommendations for each user we input
    for user_id in user_ids:

        #movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        #movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out the results
        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:3]:
            print("        %s" % x)


user_one = input('Enter user ID #1 (0 - 942):')
user_two = input('Enter user ID #2 (0 - 942):')
user_three = input('Enter user ID #3 (0 - 942):')

user_ids = (user_one, user_two, user_three)

for user_id in user_ids:
    try:
        user_id = int(user_id)
    except ValueError:
        print('Invalid input entered')
        sys.exit()
    if user_id < 0 or user_id > 942:
        print('Invalid number entered')
        sys.exit()

sample_recommendation(model, data, user_ids)