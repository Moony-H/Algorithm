import sys
input = sys.stdin.readline
_ = int(input())
arr = list(map(int, input().split()))
a = list(set(arr))
a.sort()
hash = {a[i]: i for i in range(len(a))}
for i in arr:
    print(hash[i], end=' ')