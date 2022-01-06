import copy
import sys
sys.setrecursionlimit(1000000)

def dfs(city, pos, water):
    x, y = pos
    UDLR = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    city[y][x] = -1
    for i in UDLR:
        dx = x+i[0]
        dy = y+i[1]
        if dx < 0 or dx >= len(city) or dy < 0 or dy >= len(city):
            continue
        if city[dy][dx] <= water:
            continue

        dfs(city, (dx, dy), water)
    return


INF = int(1e9)
n = int(input())
city = []

for i in range(n):
    city.append(list(map(int, input().split())))

lower = INF
higher = 0

for i in city:
    l = min(i)
    h = max(i)
    lower = min(lower, l)
    higher = max(higher, h)

answer = 0
for i in range(lower-1,higher):
    temp = copy.deepcopy(city)
    result = 0
    for j in range(len(temp)):
        for k in range(len(temp)):
            if temp[j][k] > i:
                dfs(temp, (k, j), i)
                result += 1
    answer = max(answer, result)

print(answer)