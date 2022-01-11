t = int(input())
answer = []
for i in range(t):
    n = int(input())
    cache = [1 for _ in range(n)]

    for i in range(3, n):
        cache[i] = cache[i-2]+cache[i-3]
    answer.append(cache[n-1])

for i in answer:
    print(i)
