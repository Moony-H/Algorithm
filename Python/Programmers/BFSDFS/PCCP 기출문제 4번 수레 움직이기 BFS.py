from collections import deque
import copy

def bfs(table,redPosition,bluePosition):
    #1:red, 2:blue, 3:red goal, 4:blue goal
    UDLR=[[-1,0],[1,0],[0,-1],[0,1]]
    w=len(table[0])
    h=len(table)
    vTableR=[[False for _ in range(w)] for _ in range(h)]
    vTableB=[[False for _ in range(w)]for _ in range(h)]
    table[redPosition[1]][redPosition[0]]=0
    table[bluePosition[1]][bluePosition[0]]=0

    vTableR[redPosition[1]][redPosition[0]]=True
    vTableB[bluePosition[1]][bluePosition[0]]=True
    q=deque()
    save=0
    q.append((redPosition,bluePosition,copy.deepcopy(vTableR),copy.deepcopy(vTableB),0))
    while q:
        rPo,bPo,rVisited,bVisited,turn=q.popleft()
        #succeed
        rNow=table[rPo[1]][rPo[0]]
        bNow=table[bPo[1]][bPo[0]]
        if(rNow==3 and bNow==4):
            return turn
        for i in UDLR:
            for j in UDLR:
                rdx=(rPo[0]+i[1] if rNow!=3 else rPo[0])
                rdy=(rPo[1]+i[0] if rNow!=3 else rPo[1])
                bdx=(bPo[0]+j[1] if bNow!=4 else bPo[0])
                bdy=(bPo[1]+j[0] if bNow!=4 else bPo[1])

                if(rdx<0 or rdx>=w or rdy<0 or rdy>=h):
                    continue
                if(bdx<0 or bdx>=w or bdy<0 or bdy>=h):
                    continue
                if rPo[0] == bdx and rPo[1] == bdy and \
                bPo[0]==rdx and bPo[1] == rdy:
                    continue
                if(rdx==bdx and rdy==bdy):
                    continue
                if (rVisited[rdy][rdx] and table[rdy][rdx]!=3)\
                or( bVisited[bdy][bdx] and table[bdy][bdx]!=4):
                    continue
                if(table[rdy][rdx]==5 or table[bdy][bdx]==5):
                    continue



                rTemp=copy.deepcopy(rVisited)
                bTemp=copy.deepcopy(bVisited)
                rTemp[rdy][rdx]=True
                bTemp[bdy][bdx]=True

                q.append(((rdx,rdy),(bdx,bdy),rTemp,bTemp,turn+1))

    return 0

def solution(maze):
    answer = 0
    rStart=(0,0)
    bStart=(0,0)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if(maze[i][j]==1):
                rStart=(j,i)
            if(maze[i][j]==2):
                bStart=(j,i)

    return bfs(maze,rStart,bStart)
