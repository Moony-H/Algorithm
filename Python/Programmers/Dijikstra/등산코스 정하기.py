from heapq import heappop, heappush

from collections import defaultdict

INF=int(1e9)


def di(start,graph,goals):
    distance=[INF]*(len(graph.keys())+1)
    q=[]
    
    for i in start:
        q.append([0,i])
        distance[i]=0
        
    while q:
        now_cost,node=heappop(q)
        if(node in goals):
            continue
        if(now_cost>distance[node]):
            continue
        for next,cost in graph[node]:
            next_cost=max(cost,now_cost)

            
            
            if(next_cost>=distance[next]):

                continue
            distance[next]=next_cost
            heappush(q,[next_cost,next])
    return distance
    


def solution(n, paths, gates, summits):
    answer = [0,INF]
    graph=defaultdict(list)
    results=[]
    index=0
    summit=set(summits)
    for i in paths:
        graph[i[0]].append([i[1],i[2]])
        graph[i[1]].append([i[0],i[2]])
    
    temp=di(gates,graph,summit)
    summits.sort()
    for i in summits:
        if(answer[1]>temp[i]):
            answer=[i,temp[i]]
    return answer