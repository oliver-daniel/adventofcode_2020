N = open('./in/10.txt').readlines()

N = [0] + list(sorted(map(int, N))) 

GOAL = N[-1] + 3
N.append(GOAL)

G = {}
for i, x in enumerate(N):
    G[x] = [y for y in N[i + 1: i + 4] if y - x <= 3]

def p1(): 
    def dfs(node, path = [], j1 = 0, j3 = 0):
        if node == GOAL:
            print (j1 * j3)
            return (path + [GOAL], j1, j3)
        path.append(node)
        for child in G[node]:
            if child - node == 3 and (ret := dfs(child, path, j1, j3 + 1)):
                return ret
            elif child - node == 1 and (ret := dfs(child, path, j1 + 1, j3)):
                return ret
            elif (ret := dfs(child, path, j1, j3)):
                return ret
        return None

    dfs(0)


def p2():
    import functools

    @functools.cache
    def dfs(node):
        if node == GOAL:
            return 1
        return sum(map(dfs, G[node]))

    k = dfs(0)
    print(k)

p1()
p2()
