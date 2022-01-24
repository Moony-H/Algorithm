
from itertools import combinations

n, m = map(int, input().split())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))

house = []
chicken = []
# 맵의 집과 치킨집 구하기
for i in range(n):
    for j in range(n):
        if table[i][j] == 1:
            house.append((j, i))
        if table[i][j] == 2:
            chicken.append((j, i))
INF = int(1e9)
results = []

# 치킨집의 경우의 수 모두 탐색
for chickenHouses in combinations(chicken, m):
    summ = 0
    for i in range(len(house)):
        temp = INF
        for oneChick in chickenHouses:
            # 가장 가까운 치킨집 구하기
            temp = min(
                temp, abs(oneChick[0]-house[i][0])+abs(oneChick[1]-house[i][1]))
        summ += temp
    results.append(summ)


print(min(results))
