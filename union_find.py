class Node(object):
     def __init__(self, val):
         self.val = val
         self.par = None # index of parent, not parent object itself
         self.size = 1 # only relevant for representative node in each component

class UnionFind(object):
    """Data structure that implements Union Find using a forest of trees
    with path compression and union by size
    """

    def __init__(self, vals):
        self.nodes = [Node(val) for val in vals]
        self.num_components = len(vals)

    def __str__(self):
        components = {} # maps index of representative elements to indexes of nodes in that component
        for i in range(len(self.nodes)):
            rep = self.find(i)
            if rep not in components:
                components[rep] = []
            components[rep].append(i)
        out = ""
        for rep, members in components.items():
            out += f"{rep}: {members}\n"
        return out

    def find(self, index):
        """Returns the index for the representative Node object for the component
        that the node at `index` is part of
        """
        cur = self.nodes[index]
        if cur.par is None:
            return index
        rep = self.find(cur.par)
        cur.par = rep
        return rep

    def union(self, index1, index2):
        """Merges the components that the nodes at `index1` and
        `index2` are part of
        """
        rep1 = self.find(index1)
        rep2 = self.find(index2)
        if rep1 != rep2:
            self.num_components -= 1
            node1 = self.nodes[rep1]
            node2 = self.nodes[rep2]
            if node1.size >= node2.size: # Make node2 a child of node1
                node1.size += node2.size
                node2.par = rep1
            else: # Make node1 a child of node2
                node2.size += node1.size
                node1.par = rep2
        return rep1 != rep2 # returns whether merge occurred

if __name__ == "__main__":
    uf = UnionFind([0, 1, 2, 3, 4, 5])
    assert uf.num_components == 6
    for i in range(6):
        assert i == uf.find(i)
    uf.union(0, 1)
    print(uf)
    uf.union(0, 2)
    print(uf)
    uf.union(2, 3)
    print(uf)
    uf.union(4, 5)
    print(uf)
    uf.union(3, 5)
    print(uf)
