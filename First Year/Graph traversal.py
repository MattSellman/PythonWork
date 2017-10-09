__author__ = 'Matthew'

#prims algorithm from lecture

class Graph:
    """An undirected graph with a fixed number of vertices represented by an adjacency matrix"""

    def __init__(self, size, edges = []):
        self.matrix = [[0]*size for x in range(size)]
        self.size = size
        self.edges = edges
        for edge in edges:
            if len(edge) == 2:
                self.addEdge(edge[0], edge[1], 1)
            elif len(edge) == 3:
                self.addEdge(edge[0], edge[1], edge[2])



    def vertices(graph):
        return range(graph.size)

    def addEdge(self, start, end, weight):
        self.matrix[start][end] = weight
        self.matrix[end][start] = weight

    def weight(self, start, end):
        return self.matrix[start][end]

    def connected(self, start, end):
        return self.weight(start,end) != 0

    def neighbours(self, node):
        answer = []
        for v in self.vertices():
            if self.connected(node, v):
                answer.append(v)
        return(answer)


def min (aList):
    result = aList[0]
    for m in aList[1:]:
        if m < result:
            result = m
    return result

def min2 (aList):
    result = None
    for m in aList:
        if result == None or m < result:
            result = m
    return result



def dijkstra(graph, start, end):

# set thing up: make distances and previous list and make everything unvisited

    dist = [-1] * graph.size
    previous = [-1] * graph.size
    dist[start] = 0
    unvisited = set (graph.vertices())

# the while loop chooses the next vertex to open
    while len(unvisited) != 0:
        u = None
        for v in unvisited:
            if u == None or -1 < dist[v] < dist[u]:
                u = v
        if u == end:
            break

# now chosen,  take it away from unvisites
        unvisited.remove(u)

#  The coming for loop updates all the neighbours

        for v in graph.neighbours(u):
            if v in unvisited:
                alt = dist[u] + graph.weight(u, v)
                if alt < dist[v] or dist[v] == -1:
                    dist[v] = alt
                    previous[v] = u
    if dist[end] == -1:
        return (-1, [])
    else:
        path = [end]
        v = end
        while previous[v] != -1:

            path.insert(0, previous[v])
            print('path is',path)
            v = previous[v]
        return (dist[end], path)




def prim(graph):
    if graph.size == 0:
        return Graph(0)
    result = Graph(graph.size)
    included = set([0])
    while len(included) < graph.size:
        minEdge = None
        minWeight = 0
        for v in included:
            for u in graph.neighbours(v):
                if u in included:
                    continue
                if minEdge == None or graph.weight(v, u) < minWeight:
                    print('new')
                    minWeight = graph.weight(v, u)
                    minEdge = (v, u)
                    print('min edge',v,u,'is', graph.weight(v,u))
        if minEdge == None:
            raise Exception("graph not connected")
        result.addEdge(minEdge[0], minEdge[1], minWeight)
        included.add(minEdge[1])
        print('included is', included)
    return result


def main():
    test = Graph(6, [[0,1,7],[0,2,9],[0,5,14],[1,3,15],[1,2,10],[2,3,11],
                [2,5,2],[3,4,6],[4,5,9]])

    print(dijkstra(test,0,5))

    print('****')

    myGraph = Graph(4,[[0,1,5],[0,2,4],[0,3,10],[1,3,4],[2,3,2]])
    print("adjacency matrix is", myGraph.matrix)


    print(dijkstra(myGraph,0,3))


    test2 = prim(test)
    print(test2.matrix)

main()
