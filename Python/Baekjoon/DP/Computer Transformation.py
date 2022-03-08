cache = [0 for _ in range(1001)]
cache[0] = 0
cache[1] = 0
cache[2] = 1

while True:
    try:
        n = int(input())
        for i in range(3, n+1):
            cache[i] = cache[i-1]+cache[i-2]*2
        print(cache[n])

    except EOFError:
        break
