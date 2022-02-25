
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
que = []
heappush(que, (0, x))
INF = int(1e9)
distance = [INF for _ in range(n+1)]
distance[x] = 0
while que:
    cost, node = heappop(que)
    if distance[node] < cost:
        continue
    for next_node in graph[node]:
        if distance[next_node] < cost+1:
            continue
        distance[next_node] = cost+1
        heappush(que, (cost+1, next_node))

answer = []
for i, cost in enumerate(distance):
    if cost == k:
        answer.append(i)
if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)
