import heapq


INF = int(1e9)
n, e = map(int, input().split())

table = [[]for _ in range(n)]


for i in range(e):
    a, b, cost = map(int, input().split())
    table[a-1].append((b-1, cost))
    table[b-1].append((a-1, cost))

haveToA, haveToB = map(int, input().split())


def dijkstra(start):
    q = []
    distance = [INF]*n
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in table[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


result = min(dijkstra(0)[haveToA-1]+dijkstra(haveToA-1)[haveToB-1]+dijkstra(haveToB-1)
             [n-1], dijkstra(0)[haveToB-1]+dijkstra(haveToB-1)[haveToA-1]+dijkstra(haveToA-1)[n-1])
print(result if result != INF else -1)
