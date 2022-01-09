a = int(input())
wines = []
for i in range(a):
    wines.append(int(input()))

cache = [0 for _ in range(a)]
cache[0] = wines[0]
if len(cache) == 1:
    print(cache[0])
    exit(0)
cache[1] = cache[0]+wines[1]
if len(cache) == 2:
    print(cache[1])
    exit(0)
cache[2] = max(cache[1], cache[0]+wines[2], wines[1]+wines[2])
for i in range(3, len(cache)):
    cache[i] = max(wines[i]+wines[i-1]+cache[i-3],
                   wines[i]+cache[i-2], cache[i-1])  # cache[i-1]말고 wines[i-1]+wines[i-2]+cache[i-4]로 해도 무방하다.(이쪽이 좀 더 직관적이다.)

print(cache[-1])
