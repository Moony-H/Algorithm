from collections import deque

def TopologySort(graph):
    result=[]
    que=deque()
    table=[0]*(len(graph))

    for i in graph:
        for j in i:
            table[j[0]]+=1
    for i in range(1,len(table)):
        if table[i]==0:
            que.append(i)
    while que:
        index=que.popleft()
        print(index)
        result.append(index)
        for i in graph[index]:
            table[i[0]]-=1
            if table[i[0]]==0:
                que.append(i[0])
    print(result)

n,e=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
print(graph)
TopologySort(graph)