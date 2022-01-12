n = int(input())
cache = [0 for _ in range(n+1)]
if n == 1:
    print(1)
    exit(0)
cache[1] = 1
cache[2] = 3
for i in range(3, n+1):
    cache[i] = cache[i-1]+2*cache[i-2]
print(cache[-1] % 10007)
