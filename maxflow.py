# https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
def maxflow(graph):
    '''
    Graph is an N x N adjacency matrix of capacities
    There cannot be bidirectional edges
    Source is node 0 and sink is node N - 1
    '''
    if len(graph) is not len(graph[0]):
        raise Exception("Graph must be square matrix")
    N = len(graph)
    for i in range(N):
        if graph[i][i] != 0:
            raise Exception("No flows from vertex to itself allowed")
        for j in range(i + 1, N):
            if graph[i][j] != 0 and graph[j][i] != 0:
                raise Exception("No bidirectional edges allowed")
    source = 0
    sink = N - 1
    max_flow = 0
    flows = [[0 for _ in range(N)] for _ in range(N)]
    while True:
        queue = [source]
        par = {}
        par[source] = -1
        while len(queue) > 0:
            cur = queue.pop(0)
            for v in range(N):
                if v in par:
                    continue
                if graph[cur][v] > 0 and flows[cur][v] < graph[cur][v] or graph[v][cur] > 0 and flows[v][cur] > 0:
                    par[v] = cur
                    queue.append(v)
        if sink not in par:
            break
        cur = sink
        flow = 1e9
        while par[cur] != -1:
            prev = par[cur]
            if graph[prev][cur] > 0:
                flow = min(flow, graph[prev][cur] - flows[prev][cur])
            else:
                flow = min(flow, flows[cur][prev])
            cur = prev
        cur = sink
        while par[cur] != -1:
            prev = par[cur]
            if graph[prev][cur] > 0:
                flows[prev][cur] += flow
            else:
                flows[cur][prev] -= flow
            cur = prev
        max_flow += flow
    return max_flow

graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 6, 12, 0, 0],
        [0, 0, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
print(maxflow(graph))
