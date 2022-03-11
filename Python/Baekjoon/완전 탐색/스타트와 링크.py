from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))

nums = [i for i in range(n)]
nums = set(nums)
INF = int(1e9)
answer = INF
for i in combinations(nums, n//2):
    result = 0
    for j in combinations(i, 2):
        result += table[j[0]][j[1]]+table[j[1]][j[0]]
    for j in combinations(nums-set(i), 2):
        result -= table[j[0]][j[1]]+table[j[1]][j[0]]
    answer = min(answer, abs(result))
print(answer)
