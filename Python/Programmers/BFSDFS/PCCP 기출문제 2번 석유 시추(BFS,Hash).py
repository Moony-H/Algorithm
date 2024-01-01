from collections import deque

def bfs(start,table,num):
    #y,x
    UDLR=[[-1,0],[1,0],[0,-1],[0,1]]
    q=deque()
    q.append(start)
    result=1
    table[start[1]][start[0]]=num
    
    while q:
        x,y=q.popleft()
        for i in UDLR:
            dx=x+i[1]
            dy=y+i[0]
            if(dx<0 or dx>=len(table[0]) or dy<0 or dy>=len(table)):
                continue
            if(table[dy][dx]!=1):
                continue
            table[dy][dx]=num
            result+=1
            q.append((dx,dy))
    return result

def solution(land):
    w=len(land[0])
    h=len(land)
    save={}
    num=1
    answer=0
    for i in range(w):
        results={}
        
        for j in range(h):
            if(land[j][i]==1):
                num+=1
                save[num]=bfs((i,j),land,num)
                results[num]=save[num]
            elif(land[j][i]!=0):
                results[land[j][i]]=save[land[j][i]]
        result=0
        for i in results.items():
            result+=i[1]
        answer=max(answer,result)
    return answer
