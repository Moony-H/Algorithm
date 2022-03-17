import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
answer = []
que = deque()
for i in range(1, n+1):
    que.append(i)
while len(que) != 0:
    for i in range(k-1):
        temp = que.popleft()
        que.append(temp)
    answer.append(que.popleft())

print('<', end='')
print(*answer, sep=', ', end='')
print('>')
