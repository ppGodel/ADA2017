class Vertex:
    def __init__(self, _id, _object):
        self._id =_id
        self._value = _object
        self._neighbors = {}

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value

    @property
    def neighbors(self):
        return self._neighbors.keys()

    def __str__(self):
        return 'Vertex: ' + str(self.id) + ' Neighbors: ' + str([x.id for x in self.neighbors])

    def add_neighbor(self, _neighbor, _weight=1):
        self.neighbors[_neighbor] = _weight


class Graph:
    def __init__(self):
        self.vertexs = {}
        self.cardinal = 0

    def __getitem__(self, item):
        res = None
        if isinstance(item, str):
            res = [j for i, j in enumerate(self.vertexs) if j.id== n]
        if isinstance(item, int):
            res = [j for i, j in enumerate(self.vertexs) if i== n]
        if isinstance(item, Vertex):
            res = [j for i, j in enumerate(self.vertexs) if j== n]
        print(res)
        # if n in self.vertexs:
        #    res = self.vertexs[n]
        return res

    def add_vertex(self, _vertex_obj):
        if isinstance( _vertex_obj, Vertex):
            self.vertexs[self.cardinal] = _vertex_obj
            self.cardinal += 1
        return _vertex_obj

    def __iter__(self):
        res = iter( self.vertexs.values())
        return res


    def add_edge(self, beg, end, _weight=1, directed=False):
        if end not in self.vertexs:
            self.add_vertex(end)
        if beg not in self.vertexs:
            self.add_vertex(beg)
        if not directed:
            print (str(end))
            self.vertexs[end.id].add_neighbor(self.vertexs[beg.id].id, _weight)
        self.vertexs[beg.id].add_neighbor(self.vertexs[end.id].id, _weight)

    def get_vertexs(self):
        self.vertexs.keys()


g = Graph()
a = Vertex('a', None)
b = Vertex('b', None)
c = Vertex('c', None)
d = Vertex('d', None)
e = Vertex('e', None)
f = Vertex('f', None)
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
g.add_vertex(f)

g.add_edge(a, b, 7)
g.add_edge(a, c, 9)
g.add_edge(a, f, 14)
g.add_edge(b, c, 10)
g.add_edge(b, d, 15)
g.add_edge(c, d, 11)
g.add_edge(c, f, 2)
g.add_edge(d, e, 6)
g.add_edge(e, f, 9)

for v in g:
    for n in v.neightbors():
        vid = v.get_id()
        nid = n.get_id()
        print '( %s , %s, %3d)' % (vid, nid, v.get_weight(n)) 


for v in g:
    print 'g.vertexs[%s]=%s' % (v.get_id(), g.vertexs[v.get_id()]) 



