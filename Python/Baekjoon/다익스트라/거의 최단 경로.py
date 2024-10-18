import heapq
import sys
input=sys.stdin.readline

INF=int(1e9)

def deleteRoute(graph,route):
    # [[0, 3, 6],[1, 2, 3]]
    for k in route:
        for i in range(len(k)-1):
            for j in range(len(graph[k[i]])):
                if(graph[k[i]][j][0]==k[i+1]):
                    graph[k[i]].pop(j)
                    break

def find(graph,start):
    q=[]
    distances=[[INF,[]] for _ in range(len(graph))]
    distances[start]=(0,[])

    heapq.heappush(q,(0,start,[start]))

    while q:
        cost,pos,route=heapq.heappop(q)
        for nextPos,nCost in graph[pos]:
            total=cost+nCost
            if(distances[nextPos][0]<total):
                continue
            if(distances[nextPos][0]==total):
                temp=route[:]
                temp.append(nextPos)
                distances[nextPos][0]=total
                distances[nextPos][1].append(temp)
            else:
                temp=route[:]
                temp.append(nextPos)
                distances[nextPos][0]=total
                distances[nextPos][1]=[temp]
            heapq.heappush(q,(total,nextPos,temp[:]))

    return distances

answer=[]
while True:
    N,M=map(int,input().split())
    if(N==0 and M==0):
        break
    S,D=map(int,input().split())

    graph=[[] for _ in range(N)]
    for _ in range(M):
        U,V,P=map(int,input().split())
        graph[U].append((V,P))
    
    result=find(graph,S)
    deleteRoute(graph,result[D][1])
    answerTemp=find(graph,S)
    answer.append(answerTemp[D][0])


for i in answer:
    print(i if i!=INF else -1)
