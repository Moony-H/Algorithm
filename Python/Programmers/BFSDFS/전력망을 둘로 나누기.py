def dfsSearch(node,tree,cut,visited):
    visited[node]=True
    results=0
    for i in tree[node]:
        if visited[i] or (node,i) == cut or (i,node) == cut:
            continue
        results+=dfsSearch(i,tree,cut,visited)
    return results+1
        

            

def solution(n, wires):
    answer = 999999
    nodes=[[] for _ in range(n)]
    for s,e in wires:
        nodes[s-1].append(e-1)
        nodes[e-1].append(s-1)
    for s,e in wires:
        result=dfsSearch(0,nodes,(s-1,e-1),[False]*n)
        answer=min(answer,abs(abs(n-result)-result))
    return answer