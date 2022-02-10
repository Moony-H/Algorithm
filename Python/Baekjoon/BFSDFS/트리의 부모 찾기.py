import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(start, tree, result):
    for i in tree[start]:
        if result[i] == 0:
            result[i] = start
            dfs(i, tree, result)


n = int(input())
tree = [[]for _ in range(n+1)]
result = [0 for _ in range(n+1)]
for i in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
dfs(1, tree, result)

for i in range(2, len(result)):
    print(result[i])
