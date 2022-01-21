import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

start, k = map(int, input().split())

distance = [INF]*(100001)


def dijkstra(start):
    q = []
    move = [1, -1]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        cost = dist + 1

        if distance[now] < dist:
            continue

        for i in move:
            if now+i >= len(distance) or now+i < 0:
                continue
            if cost < distance[now+i]:
                distance[now+i] = cost
                heapq.heappush(q, (cost, now+i))

        if now*2 < len(distance) and dist < distance[now*2]:
            distance[now*2] = dist
            heapq.heappush(q, (dist, now*2))
    return


if start == k:
    print(0)
    exit(0)
dijkstra(start)
print(distance[k])
