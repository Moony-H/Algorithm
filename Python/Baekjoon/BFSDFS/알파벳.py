import sys
input = sys.stdin.readline


def bfs(graph, r, c):
    q = set([(0, 0, graph[0][0])])
    UDLR = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    result = 0
    while q:
        x, y, way = q.pop()
        result = max(result, len(way))
        for i in UDLR:
            dx = x+i[0]
            dy = y+i[1]

            if dx < 0 or dy < 0 or dx >= c or dy >= r:
                continue
            if graph[dy][dx] in way:
                continue
            q.add((dx, dy, way+graph[dy][dx]))
    return result


r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))
print(bfs(graph, r, c))
