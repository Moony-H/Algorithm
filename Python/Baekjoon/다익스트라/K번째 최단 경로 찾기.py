import heapq
import sys

input=sys.stdin.readline

def findGraph(graph,start,k):
    pq=[]
    table=[[] for _ in range(len(graph))]
    heapq.heappush(pq,(0,start))
    heapq.heappush(table[start],0)
    while pq:
        cost,node=heapq.heappop(pq)
        for nextNode,dCost in graph[node]:
            totalCost=cost+dCost
            if(len(table[nextNode])<k):
                heapq.heappush(table[nextNode],-totalCost)
                heapq.heappush(pq,(totalCost,nextNode))
            
            elif(abs(table[nextNode][0])>totalCost):
                heapq.heappop(table[nextNode])
                heapq.heappush(table[nextNode],-totalCost)
                heapq.heappush(pq,(totalCost,nextNode))


    return table

n,m,k=map(int,input().split())

graph=[[] for _ in range(n)]

for _ in range(m):
    s,e,c=map(int,input().split())
    graph[s-1].append((e-1,c))

table=findGraph(graph,0,k)

for i in table:
    if(len(i)==k):
        print(abs(i[0]))
        continue
    print(-1)
