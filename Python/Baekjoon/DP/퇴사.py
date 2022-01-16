N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

cache = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    t, p = arr[i]
    if t+i > N:
        cache[i] = cache[i+1]
        continue
    cache[i] = max(cache[i+t]+p, cache[i+1])

print(cache[0])
