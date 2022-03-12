import sys
input = sys.stdin.readline


n = int(input())
answer = [-1 for _ in range(n)]
a = list(map(int, input().split()))
arr = [[a[i], i]for i in range(n)]
stack = []

for i in arr:

    if len(stack) == 0:
        stack.append(i)
        continue
    while len(stack) != 0 and stack[-1][0] < i[0]:
        temp = stack.pop()
        answer[temp[1]] = i[0]
    stack.append(i)
print(*answer)
