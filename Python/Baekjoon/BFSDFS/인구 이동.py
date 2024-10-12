from collections import deque
import sys

def open(graph,start,L,R,flag,opened):
    UDLR=[[0,-1],[0,1],[-1,0],[1,0]]
    q=deque()
    q.append(start)
    length=len(graph)
    isRepeat=False
    while q:
        pos=q.popleft()
        for dx,dy in UDLR:

            newX=dx+pos[0]
            newY=dy+pos[1]
            if newX>=length or newX<0 or newY>=length or newY<0:
                continue
            if(opened[newY][newX]!=0):
                continue
            diff=abs(graph[newY][newX]-graph[pos[1]][pos[0]])
            if diff<L or diff>R:
                continue
            if not isRepeat:
                isRepeat=True
                opened[pos[1]][pos[0]]=flag
            opened[newY][newX]=flag
            q.append((newX,newY))
    return isRepeat
    

def mix(opened,graph):
    hash={}
    for i in range(len(opened)):
        for j in range(len(opened[i])):
            if(opened[i][j]==0):
                continue
            temp=hash.get(opened[i][j],[0,0])
            temp[0]+=graph[i][j]
            temp[1]+=1
            hash[opened[i][j]]=temp
    
    for i in hash.keys():
        hash[i][0]=int(hash[i][0]/hash[i][1])

    if len(hash.keys())==0:
        return
    for i in range(len(opened)):
        for j in range(len(opened)):
            if(opened[i][j]==0):
                continue
            temp=hash[opened[i][j]]
            graph[i][j]=temp[0]


    

def allZero(opened):
    for i in opened:
        for j in i:
            if(j!=0):
                return False
    return True



input= sys.stdin.readline

N,L,R=map(int,input().split())

graph=[]

for _ in range(N):
    graph.append(list(map(int,input().split())))


count=0
while True:
    done=1
    opened=[[0 for _ in range(N)]for _ in range(N)]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if(opened[i][j]!=0):
                continue
            if(open(graph,(j,i),L,R,done,opened)):
                done+=1
    if(allZero(opened)):
        break
    mix(opened,graph)
    count+=1

print(count)