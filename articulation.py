def articulate(adj):
    '''
    Given adjacency matrix for connected, undirected graph, returns all articulation points
    Algorithm:
    1. Generate DFS tree
    2. For each node, compute lowest (min height) node reacheable from that nodes subtree
    3. Root is articulation point iff has at least two children
    4. All other nodes are articulation point iff at least one children cannot reach a lower node than it
    '''

    if len(adj) != len(adj[0]):
        raise ValueError("Adjacency matrix must be square")

    N = len(adj)
    par = {}
    vis = [] # finish order
    depth = {}
    back = [] # backedges in DFS tree

    source = 0
    par[source] = -1
    depth[source] = 0

    def dfs(v):
        for u in range(N):
            if adj[u][v]:
                if u in par:
                    back.append((v, u)) # edges are taken from v to u
                else:
                    par[u] = v
                    depth[u] = depth[v] + 1
                    dfs(u)
        vis.append(v)

    dfs(source)

    if len(par) < N:
        raise ValueError("Input must be connected graph")

    children = {}
    for u in par:
        v = par[u]
        if v not in children:
            children[v] = []
        children[v].append(u)

    top = {} # stores min depth reachable by backedge from subtree
    for v in range(N):
        top[v] = depth[v]
    for v, u in back:
        top[v] = min(top[v], depth[u])

    art_pts = []
    for v in vis:
        if v != source:
            art = False
            if v in children:
                for c in children[v]:
                    if top[c] >= depth[v]:
                        art = True
                    top[v] = min(top[v], top[c])
            if art:
                art_pts.append(v)

    if len(children[source]) >= 2:
        art_pts.append(source)

    return art_pts

adj = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]
print(articulate(adj))
