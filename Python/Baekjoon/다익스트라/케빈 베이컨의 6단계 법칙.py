import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
rel = [[INF for _ in range(n)]for _ in range(n)]

for i in range(m):
    s, e = map(int, input().split())
    rel[s-1][e-1] = 1
    rel[e-1][s-1] = 1

for i in range(n):
    rel[i][i] = 0


for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            rel[j][k] = min(rel[j][k], rel[j][i]+rel[i][k])
result = INF
answer = 0
for i in range(n):
    if result > sum(rel[i]):
        result = sum(rel[i])
        answer = i+1
print(answer)
