from collections import deque
import copy

def bfs(table,start,end):
    UDLR=[[-1,0],[1,0],[0,-1],[0,1]]
    que=deque()
    v=[[False for _ in range(len(table[0]))]for _ in range(len(table))]
    v[start[1]][start[0]]=True
    que.append((start[0],start[1],0,v))
    
    
    while que:
        x,y,cost,visited=que.popleft()
        if(table[y][x]==end):
            return cost
        for i in UDLR:
            dx=x+i[1]
            dy=y+i[0]
            if(dx<0 or dx>=len(table[0]) or dy<0 or dy>=len(table)):
                continue
            if(table[dy][dx]=='X'):
                continue
            if(visited[dy][dx]):
                continue
            visited[dy][dx]=True
            que.append((dx,dy,cost+1,visited))
    return -1
            
        

def solution(maps):
    answer = 0
    start=()
    switch=()
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if(maps[i][j]=='S'):
                start=(j,i)
            if(maps[i][j]=='L'):
                switch=(j,i)
    switchCost=bfs(maps,start,'L')
    if(switchCost==-1):
        return -1
    endCost=bfs(maps,switch,'E')
    if(endCost==-1):
        return -1
    return switchCost+endCost