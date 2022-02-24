from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
bus = int(input())

graph = [[]for _ in range(n+1)]

for i in range(bus):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))

start, end = map(int, input().split())

que = []
heappush(que, (0, start, [start]))
distance = [INF for _ in range(n+1)]
distance[start] = 0

while que:
    cost, node, path = heappop(que)
    if node == end:
        print(distance[end])
        print(len(path))
        print(*path)
        break
    if distance[node] < cost:
        continue
    for i in graph[node]:
        if distance[i[0]] < cost+i[1]:
            continue
        distance[i[0]] = cost+i[1]
        heappush(que, (distance[i[0]], i[0], path+[i[0]]))
