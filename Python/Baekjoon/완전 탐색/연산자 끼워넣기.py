import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
maximum = -int(1e9)
minimum = int(1e9)
n = 0


def dfs(p, m, mul, d, result, arr, depth):
    global maximum
    global minimum
    global n

    if depth == n:
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return
    if p > 0:

        dfs(p-1, m, mul, d, result+arr[depth], arr, depth+1)
    if m > 0:

        dfs(p, m-1, mul, d, result-arr[depth], arr, depth+1)
    if mul > 0:

        dfs(p, m, mul-1, d, result*arr[depth], arr, depth+1)
    if d > 0:

        dfs(p, m, mul, d-1, int(result/arr[depth]), arr, depth+1)


n = int(input())
arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

dfs(plus, minus, mul, div, arr[0], arr, 1)
print(maximum)
print(minimum)
