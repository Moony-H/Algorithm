import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
que = deque()
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))
answer = 0
time = -1
for i in arr:
    if time <= i[0]:
        time = i[1]
        answer += 1

print(answer)