from collections import deque
import sys

input = sys.stdin.readline


def bfs(table, start, startSize):
    ULRD = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    l = len(table)
    visited = [[False for _ in range(l)]for _ in range(l)]
    que = deque()
    que.append((start[0], start[1], startSize, 0))
    result = []
    while que:
        x, y, size, time = que.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True
        if table[y][x] != 9 and table[y][x] != 0 and table[y][x] < size:
            if len(result) == 0:
                result.append((x, y, time))
            elif result[0][2] == time:
                result.append((x, y, time))
            else:
                break

            continue
        for i in ULRD:
            dx = i[1]+x
            dy = i[0]+y
            if dx < 0 or dx >= l or dy < 0 or dy >= l:

                continue
            if table[dy][dx] > size:
                continue

            que.append((dx, dy, size, time+1))
    if len(result) == 0:
        return (-1, -1, 0)
    else:
        return sorted(result, key=lambda x: (x[2], x[1], x[0]))[0]


n = int(input())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))

x, y = (0, 0)
for i in range(n):
    for j in range(n):
        if table[i][j] == 9:
            x = j
            y = i
            table[i][j] = 0

answer = 0
size = 2
ate = 0

while True:
    result = bfs(table, (x, y), size)
    pos = (result[0], result[1])
    if pos == (-1, -1):
        break
    else:
        answer += result[2]
        x = pos[0]
        y = pos[1]
        ate += 1
        table[y][x] = 0
        if ate == size:
            size += 1
            ate = 0


print(answer)
