import gzip
from scipy.sparse import coo_matrix

my_artist = input('Who\'s your favorite artist? ')
my_artist2 = input('Who\'s your second favorite artist? ')
my_artist3 = input('Who\'s your third favorite artist? ')

def get_lastfm(min_plays=200):

    # [plays], [user_index], [artist_index]
    data, row, col = [], [], []

    # {artist_id: {'id': 'index', 'name': 'artist_name'}}
    artists = {}

    # {user_id: 'index'}
    users = {}

    # open data set
    musicFile = gzip.open('/Users/brettgadberry/Desktop/lastfm-dataset-360K.tar.gz', 'rt')
    
    # skip header
    iter_musicFile = iter(musicFile)
    next(iter_musicFile)

    # read data set
    for n, line in enumerate(iter_musicFile):
        readable_data  = line.split('\t')
        user_id = readable_data[0]
        artist_id = readable_data[1]
        artist_name = readable_data[2]
        plays = int(readable_data[3])
        
        # add user to users dictionary 
        if user_id not in users:
            users[user_id] = len(users)
        
        # add artist to artists dictionary 
        if artist_id not in artists:
            artists[artist_id] = {
                'name' : artist_name,
                'id' : len(artists)
                }
        
        # add data to coo_matrix
        if plays > min_plays:
            data.append(plays)
            row.append(users[user_id])
            col.append(artists[artist_id]['id'])

        # end function at n rows
        if n == 180000: break
    
    my_user_id = '0000000000000000000000000000000000000000'
    users[my_user_id] = len(users)

    for artist in artists.items():
        if len(data) == 51367: break
        if my_artist == artist[1]['name']:
            data.append(500)
            row.append(len(users))
            col.append(artist[1]['id'])
            print('%s found' % my_artist)
            continue
        elif my_artist2 == artist[1]['name']:
            data.append(400)
            row.append(len(users))
            col.append(artist[1]['id'])
            print('%s found' % my_artist2)
            continue
        elif my_artist3 == artist[1]['name']:
            data.append(300)
            row.append(len(users))
            col.append(artist[1]['id'])
            print('%s found' % my_artist3)

    # complie matrix
    coo = coo_matrix((data,(row,col)))

    # return matrix, artists dictionary, amount of users
    dictionary = {
        'matrix' : coo,
        'artists' : artists,
        'users' : len(users)
        }

    return dictionary