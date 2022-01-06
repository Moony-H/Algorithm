
from collections import deque

m,n=map(int,input().split())
array=[]
for i in range(m):
    array.append(list(map(int,input())))

que=deque()
que.append((0,0))

UDLR=[[-1,0],[1,0],[0,-1],[0,1]]

while que:
    y,x=que.popleft()
    for i in UDLR:
        dy=y+i[0]
        dx=x+i[1]
        if dy>=m or dy<0 or dx>=n or dx<0:
            continue
        if array[dy][dx]==0:
            continue
        if array[dy][dx]==1:
            array[dy][dx]=array[y][x]+1
            que.append((dy,dx))
print(array[m-1][n-1])