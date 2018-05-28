# http://people.csail.mit.edu/indyk/6.838-old/handouts/lec17.pdf
INF = 1e9

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def min_dist(points):
    '''
    Given list of points represented as (x, y), returns the shortest distance between any pair of points
    '''
    pts_x = sorted(points, key=lambda p: p[0]) # points sorted by x coordinate
    pts_y = sorted(points, key=lambda p: p[1]) # points sorted by y coordinate

    # divide and conquer
    def solve(i, j):
        '''
        Solves the problem for points from index i to index j
        '''
        if i >= j:
            return INF
        m = (i + j) // 2
        left = solve(i, m)
        right = solve(m + 1, j)
        best = min(left, right)

        med = (pts_x[m][0] + pts_x[m + 1][0]) / 2

        candidates = []
        for x, y in pts_y:
            if abs(x - med) <= best:
                candidates.append((x, y))

        for i in range(len(candidates)):
            j = i + 1
            while j < len(candidates) and candidates[j][1] <= candidates[i][1] + best:
                best = min(best, dist(candidates[i], candidates[j]))
                j += 1

        return best

    return solve(0, len(points) - 1)

points = [
    (0, 0),
    (1, 100),
    (2, -50),
    (3, 2)
]

print(min_dist(points))
