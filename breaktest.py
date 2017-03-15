from pprint import pprint

a = [('It', 'PRP', 1, False),
 ('possessed', 'VBD', 2, True),
 ('a', 'DT', 1, False),
 ('proconsul', 'NN', 3, True),
 ('rather', 'RB', 2, True),
 ('than', 'IN', 1, False),
 ('an', 'DT', 1, False),
 ('urban', 'JJ', 2, True),
 ('prefect', 'NN', 2, True)]

for x in xrange(0,len(a)):
    if a[x][3] != True:
        a[x] += ({},)
        continue

    a[x] += ({'syn':[]},)

pprint(a)
