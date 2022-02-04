import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline


def dijkstra(table):
    distance = [[INF for _ in range(len(table))]for _ in range(len(table))]
    distance[0][0] = table[0][0]
    que = []
    heapq.heappush(que, (table[0][0], 0, 0))
    UDLR = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    while que:
        cost, x, y = heapq.heappop(que)
        if x == len(table)-1 and y == len(table)-1:
            break
        if distance[y][x] < cost:
            continue
        for i in UDLR:
            dx = x+i[0]
            dy = y+i[1]
            if dx < 0 or dx >= len(table) or dy < 0 or dy >= len(table):
                continue
            if distance[dy][dx] < table[dy][dx]+cost:
                continue
            distance[dy][dx] = cost+table[dy][dx]
            heapq.heappush(que, (distance[dy][dx], dx, dy))
    return distance[-1][-1]


answers = []
while True:
    n = int(input())
    if n == 0:
        break
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))
    answers.append(dijkstra(table))

for i in range(len(answers)):
    print('Problem {}: {}'.format(i+1, answers[i]))
