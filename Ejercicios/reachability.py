def reachability(G, a, b):
    d = dict()
    with open(G, 'r') as lol:
        for l in lol:
            e = (l.strip()).split()
            x, y = e.pop(), e.pop()
            r = d.get(x, {x}) | d.get(y, {y})
            if a in r and b in r:
                return True
            for v in r:
                d[v] = r
            print(d)
    return False

print(reachability("lol.dat", '5', '3'))
