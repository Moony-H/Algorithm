import heapq



def dijikstra(graph,start):
    table=[int(1e9) for _ in range(len(graph))]
    que=[]
    heapq.heappush(que,(0,start))

    table[start]=0
    while que:
        now,index=heapq.heappop(que)
        for i in graph[index]:
            node,cost=i
            if table[node]>cost+now:
                table[node]=cost+now
                heapq.heappush(que,(table[node],node))
    return table
n,e=map(int,input().split())
start=int(input())

graph=[[] for _ in range(n+1)]
for i in range(e):
    node,target,cost=map(int,input().split())
    graph[node].append((target,cost))
print(dijikstra(graph,start))
