from glob import glob
g = [f for f in glob('*.py') if f[0].isdigit()]
g.sort(key=lambda x: int(x.split('.')[0]))

for i, x in enumerate(g, start=1):
    print(f'Day {i}:')
    exec(open(x).read())
    print('--------')