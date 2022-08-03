from heapq import heappop, heappush
import sys

input=sys.stdin.readline
n=int(input())
que=[]
for i in range(n):
    cmd=int(input())
    if cmd==0:
        if len(que)==0:
            print(0)
        else:
            print(-heappop(que))
    else:
        heappush(que,-cmd)
