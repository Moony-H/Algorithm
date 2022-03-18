import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
que = deque()
for i in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push_front':
        que.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        que.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif cmd[0] == 'pop_back':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop())
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    else:
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
