n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

cache = [0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i+1):
        cache[i] = max(cache[i-j]+arr[j], cache[i])
print(cache[-1])
