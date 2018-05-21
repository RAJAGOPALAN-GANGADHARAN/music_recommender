import gzip
from scipy.sparse import coo_matrix


# coo_matrix
data, row, col = [], [], []

artists, users = {}, {}

min_plays = 200

musicFile = gzip.open('/Users/brettgadberry/Desktop/lastfm-dataset-360K.tar.gz', 'rt')

iter_musicFile = iter(musicFile)
next(iter_musicFile)

for n, line in enumerate(iter_musicFile):
    readable_data  = line.split('\t')
    user = readable_data[0]
    artist_id = readable_data[1]
    artist_name = readable_data[2]
    plays = int(readable_data[3])
    
    if user not in users:
        users[user] = len(users)

    if artist_id not in artists:
        artists[artist_id] = {
            'name' : artist_name,
            'id' : len(artists)
            }

    if plays > min_plays:
        data.append(plays)
        row.append(users[user])
        col.append(artists[artist_id]['id'])
    
    if n == 100000: break

coo = coo_matrix((data,(row,col)))

dictionary = {
    'matrix' : coo,
    'artists' : artists,
    'users' : len(users)
    }

print("hello world")