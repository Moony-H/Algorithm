from collections import deque
import sys

def open(graph,start,L,R):
    UDLR=[[0,-1],[0,1],[-1,0],[1,0]]
    q=deque(start)
    result=[[False for _ in range(len(graph[i]))]for i in range(len(graph))]
    isRepeat=False
    while q:
        pos=q.popleft()
        for dx,dy in UDLR:
            newX=dx+pos[0]
            newY=dy+pos[1]
            diff=abs(graph[newY][newX]-graph[pos[1]][pos[0]])
            if(result[newY][newX]):
                continue
            if diff<L or diff>R:
                continue
            if not isRepeat:
                isRepeat=False
                result[pos[1]][pos[0]]=True
            result[newY][newX]=True
            q.append((newX,newY))
    return result
    

def mix(result,graph):
    sum=0
    count=0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if(result[i][j]):
                sum+=graph[i][j]
                count+=1
    
    sum=int(sum/count)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if(result[i][j]):
                graph[i][j]=sum





input= sys.stdin.readline

N,L,R=map(int,input().split())

graph=[]

for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(len(graph)):
    for j in range(len(graph)):
        

