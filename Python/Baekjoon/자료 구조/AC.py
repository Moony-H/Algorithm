import sys
from collections import deque
input=sys.stdin.readline

T=int(input().rstrip())

for _ in range(T):
    cmd=input().rstrip()
    n=int(input().rstrip())

    text=input().rstrip()[1:-1].split(',')
    arr=deque(text)

    if(n==0):
        arr=[]

    errored=False
    reverse=False
    for i in cmd:
        if i=='R':
            reverse=not reverse
            
        else:
            if len(arr)==0:
                print('error')
                errored=True
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if(errored):
        continue
    
    if(reverse):
        arr.reverse()
        print('['+','.join(arr)+']')
    else:
        
        print('['+','.join(arr)+']')
