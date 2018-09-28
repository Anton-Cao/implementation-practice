import unittest
from heap import Heap
from union_find import UnionFind

def kruskals(N, edges):
    """Returns a list of edges of the graph that make up a minimum spanning tree using Kruskal's algorithm.
    N (int): the number of nodes in the graph
    edges [(int, int, float)]: the edges in the graph represented as (node1, node2, weight) where 0 <= node < N
    """
    UF = UnionFind(list(range(N))) # create union find data structure on the nodes
    edges.sort(key=lambda edge: edge[2]) # sort edges by increasing weight
    mst = [] # will store list of edges
    for edge in edges:
        if UF.union(edge[0], edge[1]):
            mst.append(edge)
    if len(mst) < N - 1: # graph was not connected
        return False
    return mst

def prims(N, edges):
    """Returns a list of edges of the graph that make up a minimum spanning tree using Prim's algorithm.
    N (int): the number of nodes in the graph
    edges [(int, int, float)]: the edges in the graph represented as (node1, node2, weight) where 0 <= node < N
    """
    edge_map = {} # turn list of edges into a map of node to edges
    for n in range(N):
        edge_map[n] = []
    for edge in edges:
        edge_map[edge[0]].append((edge[0], edge[1], edge[2]))
        edge_map[edge[1]].append((edge[1], edge[0], edge[2]))

    H = Heap(key=lambda edge: edge[2]) # stores edges in increasing weight
    vis = [False] * N
    vis[0] = True # start at node 0 arbitrarily
    for edge in edge_map[0]:
        H.push(edge)
    mst = []
    while len(H) > 0:
        cur = H.pop()
        if not vis[cur[1]]:
            vis[cur[1]] = True
            mst.append(cur)
            for edge in edge_map[cur[1]]:
                H.push(edge)
    if len(mst) < N - 1:
        return False
    return mst

class TestHeap(unittest.TestCase):
    def test_kruskals(self):
        N = 5
        edges = [(0, 1, 3), (1, 3, 7), (0, 2, 5), (0, 4, 10), (1, 2, 8), (2, 4, 8), (1, 4, 6), (3, 4, 2)]
        mst = kruskals(N, edges)
        self.assertEqual(len(mst), N - 1)
        self.assertEqual(sum([edge[2] for edge in mst]), 16)

    def test_prims(self):
        N = 5
        edges = [(0, 1, 3), (1, 3, 7), (0, 2, 5), (0, 4, 10), (1, 2, 8), (2, 4, 8), (1, 4, 6), (3, 4, 2)]
        mst = prims(N, edges)
        self.assertEqual(len(mst), N - 1)
        self.assertEqual(sum([edge[2] for edge in mst]), 16)

if __name__ == "__main__":
    res = unittest.main(verbosity = 3, exit = False)

