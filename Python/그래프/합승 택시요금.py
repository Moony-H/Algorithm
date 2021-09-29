def solution(n, s, a, b, fares):
    INF=int(1e9)
    answer = INF
    table=[[INF for _ in range(n+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        table[i][i]=0
    for i in fares:
        table[i[0]][i[1]]=i[2]
        table[i[1]][i[0]]=i[2]
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if j!=k:
                    table[j][k]=min(table[j][k],table[j][i]+table[i][k])
    for i in range(1,n+1):
        answer=min(answer,table[s][i]+table[i][a]+table[i][b])
    
        
    
    return answer