import itertools as it

CARD_PK = 15335876
DOOR_PK = 15086442

def transform(subj, sz):
    return pow(subj, sz, 20201227)

def loop_sizes(pk):
    for i in it.count(start=6):
        if transform(7, i) == pk:
            yield i


for x, y in zip(loop_sizes(CARD_PK), loop_sizes(DOOR_PK)):
    if (k := transform(CARD_PK, y)) == transform(DOOR_PK, x):
        print('Found!', k)
        break
    else:
        print('No good', x, y)




