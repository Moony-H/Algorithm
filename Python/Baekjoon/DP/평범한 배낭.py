import sys
input = sys.stdin.readline
N, K = map(int, input().split())
stuff = [[0, 0]]
cache = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            cache[i][j] = cache[i - 1][j]
        else:
            cache[i][j] = max(value + cache[i - 1]
                              [j - weight], cache[i - 1][j])

print(cache[N][K])
