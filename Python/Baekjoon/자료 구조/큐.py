import sys
input = sys.stdin.readline

q = []
n = int(input())
answer = []
for i in range(n):
    cmd = input().split()
    if 'push' == cmd[0]:
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(q) == 0:
            print(-1)
            continue
        print(q[0])
        del q[0]
    elif cmd[0] == 'back':
        if len(q) == 0:
            print(-1)
            continue
        print(q[-1])
    elif cmd[0] == 'front':
        if len(q) == 0:
            print(-1)
            continue
        print(q[0])
    elif cmd[0] == 'size':
        print(len(q))
    else:
        if len(q) == 0:
            print(1)
        else:
            print(0)
