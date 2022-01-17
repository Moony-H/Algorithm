import sys
sys.setrecursionlimit(100000)


def dfs(table, start, rectangle):
    count = 1
    x, y = start
    if x < 0 or y < 0 or x >= len(table[0]) or y >= len(table):
        return 0
    if table[y][x]:
        return 0
    for lx, ly, rx, ry in rectangle:
        if lx <= x and ly <= y and rx > x and ry > y:
            return 0

    table[y][x] = True
    UDLR = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    for i in UDLR:
        dx = x+i[0]
        dy = y+i[1]
        count += dfs(table, (dx, dy), rectangle)
    return count


rectangle = []
m, n, k = map(int, input().split())
table = [[False for _ in range(n)]for _ in range(m)]
for i in range(k):
    rectangle.append(list(map(int, input().split())))

area = 0
width = []
for i in range(m):
    for j in range(n):
        temp = dfs(table, (j, i), rectangle)
        if temp != 0:
            area += 1
            width.append(temp)
print(area)
width.sort()
for i in width:
    print(i, end=' ')
