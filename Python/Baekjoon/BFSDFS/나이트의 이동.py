from collections import deque


def bfs(table, start, destination):

    directions = [[-1, -2], [1, -2], [-2, -1],
                  [-2, 1], [1, 2], [-1, 2], [2, -1], [2, 1]]
    if start == destination:
        return 0
    que = deque()
    que.append((start[0], start[1], 0))
    while que:
        x, y, count = que.popleft()
        for i in directions:
            dx = x+i[0]
            dy = y+i[1]

            if dx < 0 or dy < 0 or dx >= len(table) or dy >= len(table):
                continue
            if table[dy][dx]:
                continue
            if dx == destination[0] and dy == destination[1]:
                return count+1
            table[dy][dx] = True
            que.append((dx, dy, count+1))
    return -1


answer = []
case = int(input())
for i in range(case):
    l = int(input())
    table = [[False for _ in range(l)]for _ in range(l)]
    start = list(map(int, input().split()))
    destination = list(map(int, input().split()))
    answer.append(bfs(table, start, destination))

for i in answer:
    print(i)
