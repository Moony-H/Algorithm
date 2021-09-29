from collections import deque
from itertools import combinations
import copy

INF=int(1e9)


def bfs(lab,start):
    que=deque()
    que.append(start)
    result=1
    UDLR=[[-1,0],[1,0],[0,-1],[0,1]]
    while que:
        x,y=que.popleft()

        
        for i in UDLR:
            dx=x+i[1]
            dy=y+i[0]
            if dx<0 or dy<0 or dx>=len(lab[0]) or dy>=len(lab):
                continue
            if lab[dy][dx]==1:
                continue
            if lab[dy][dx]==2:
                continue
            result+=1
            lab[dy][dx]=1
            que.append((dx,dy))
    return result



n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

cases=[]
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j]==0:
            cases.append([i,j])

safe=0
for i in combinations(cases,3):
    temp=copy.deepcopy(graph)
    
    for j in i:
        temp[j[0]][j[1]]=1
    #for j in graph:
    #    print(j)
    #print()
    for j in range(len(temp)):
        for k in range(len(temp[j])):
            if temp[j][k]==2:
                bfs(temp,(k,j))
    result=0
    for j in range(len(temp)):
        for k in range(len(temp[j])):
            if temp[j][k]==0:
                result+=1
                
    safe=max(safe,result)

print(safe)












    





        
