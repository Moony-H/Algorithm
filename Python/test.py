import sys

from collections import deque


def bfs(start,table):
    UDLR=[[0,-1],[0,1],[-1,0],[1,0]]
    q=deque()
    q.append((start[0],start[1],[],0))
    result=0
    while q:

        x,y,visited,cost=q.popleft()
        if(len(visited)>=4 and result<cost):
            result=cost
            continue
        for i in UDLR:
            dx=x+i[0]
            dy=y+i[1]
            if(dx<0 or dx>=len(table[0]) or dy<0 or dy>=len(table)):
                continue
            if(dx,dy) in visited:
                continue
            q.append((dx,dy,[i for i in visited]+[dx,dy],cost+table[dy][dx]))
    return result




input=sys.stdin.readline

n,m=map(int,input().split())
table=[]
for i in range(n):
    table.append(list(map(int,input().split())))


#for i in range(case):
#    n,m=map(int,input().rstrip().split())
#    print(solution(n,m))


