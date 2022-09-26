
from collections import deque

def bfs(table,red,blue):
    q=deque()
    q.append((red[0], red[1],blue[0],blue[1], 0))

    UDLR=[[0,-1],[0,1],[-1,0],[1,0]]
    while q:
        rx,ry,bx,by,num=q.popleft()
        if num>10:
            return -1
        if table[by][bx]=="O":
            continue
        if table[ry][rx]=='O':
            return num
        for i in range(len(UDLR)):
            dbx=bx+UDLR[i][0]
            dby=by+UDLR[i][1]
            drx=rx+UDLR[i][0]
            dry=ry+UDLR[i][1]
            if table[dby][dbx]=='#':
                dbx=bx
                dby=by
            if table[dry][drx]=='#':
                drx=rx
                dry=ry
            
            if drx==dbx and dby==dry:
                if i==0:
                    if ry>by:
                        dry=ry
                    else:
                        dby=by
                if i==1:
                    if ry>by:
                        dby=by
                    else:
                        dry=ry
                if i==2:
                    if bx>rx:
                        dbx=bx
                    else:
                        drx=rx
                else:
                    if bx>rx:
                        drx=rx
                    else:
                        dbx=bx
            q.append((drx,dry,dbx,dby,num+1))


n,m=map(int,input().rstrip().split())
table=[]
for _ in range(n):
    table.append(list(input()))

startR=()
startB=()
for i in range(n):
    for j in range(m):
        if table[i][j]=='R':
            startR=(j,i)
            table[i][j]='.'
        if table[i][j]=='B':
            startB=(j,i)
            table[i][j]='.'
print(bfs(table,startR,startB))


