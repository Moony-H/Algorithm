def w(a, b, c, cache):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20, cache)
    if cache[a][b][c] != 0:
        return cache[a][b][c]
    if a < b and b < c:
        cache[a][b][c] = w(a, b, c-1, cache) + \
            w(a, b-1, c-1, cache)-w(a, b-1, c, cache)
        return cache[a][b][c]
    cache[a][b][c] = w(a-1, b, c, cache) + w(a-1, b-1, c, cache) + \
        w(a-1, b, c-1, cache) - w(a-1, b-1, c-1, cache)
    return cache[a][b][c]


cache = [[[0 for _ in range(21)]for _ in range(21)]for _ in range(21)]
while True:
    a, b, c = map(int, input().split())
    if a == b and b == c and a == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c, cache)))
