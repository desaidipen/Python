def sorting_hotels(stdin):
    """ Sorting Hotels """
    d = {}
    df = {}

    # Gathering All Data and Rating
    for i in range(len(stdin)):
        b = stdin[i].split(' ')
        if i > 0:
            # print ('{0} --- {1} --- {2}'.format(i, b[0], b[1]))
            try:
                d[b[0]][0] = int(d.get(b[0])[0]) + int(b[1])
                d[b[0]][1] = d.get(b[0])[1] + 1
            except Exception:
                d[b[0]] = [b[1], 1]
    # print ('{0} > Length: {1}'.format(d, len(d)))

    # Finding an Average Rating
    hotels = d.keys()
    for i in range(len(d)):
        df[hotels[i]] = float(float(d[hotels[i]][0]) / float(d[hotels[i]][1]))
    # print ('{0} > Length: {1}'.format(df, len(df)))

    # Sorting Hotels
    hotels = df.keys()
    ratings = df.values()

    for i in range(len(hotels)):
        hotels.insert(0, hotels.pop(ratings.index(min(ratings[i:]), i)))
        ratings.insert(0, ratings.pop(ratings.index(min(ratings[i:]), i)))
    # print ('SORTED: {0}'.format(hotels))
    # print ('SORTED: {0}'.format(ratings))

    for hotel in hotels:
        print (hotel)

stdin = ['4', '1000 8', '2000 8', '2000 10', '1000 9', '3000 5', '3000 7', '3000 3', '2000 9', '1000 4', '5000 7']
sorting_hotels(stdin)


import itertools

def combinations(s):
    # print ('Length: {0}'.format(len(s)))
    for i in range(1, len(s)+1):
        for subset in itertools.combinations(s, i):
            print(subset)

s = 'abcdefghijklmnopqr'
combinations(s)
