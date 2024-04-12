from collections import deque

UDLR=[[0,-1],[0,1],[-1,0],[1,0]]
def move(table,position,dirInt):
    global UDLR
    posX,posY=position
    direction=UDLR[dirInt]
    while posX<len(table[0]) and\
    posX>=0 and posY>=0 and\
    posY<len(table) and\
    table[posY][posX] !='D':
        posX+=direction[0]
        posY+=direction[1]
    return (posX-direction[0],posY-direction[1])

        
def bfs(table,start):
    visited=[[0 for _ in table[0]] for _ in table]
    que=deque()
    que.append((start,0))
    global UDLR
    while que:
        position,count=que.popleft()
        if table[position[1]][position[0]]=='G':
            return count
        for i in range(len(UDLR)):
            dx,dy=move(table,position,i)
            if visited[dy][dx]!=0 and visited[dy][dx]<=count:
                continue
            visited[dy][dx]=count
            que.append(((dx,dy),count+1))
    return -1
    
def solution(board):
    answer = 0
    start=(0,0)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='R':
                start=(j,i)
                break
            
    answer=bfs(board,start)
    return answer