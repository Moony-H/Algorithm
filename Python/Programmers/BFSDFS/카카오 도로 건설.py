from collections import deque

def solution(board):
    UDLR=[[-1,0],[1,0],[0,-1],[0,1]]
    boardSize=len(board)
    visited=[]
    for i in board:
        newArr=[]
        for _ in i:
            newArr.append(False)
        visited.append(newArr)
    print(visited)
    answer=99999999
    que=deque()
    que.append((0,1,0,0))
    que.append((0,3,0,0))
    while que:
        cost,direction,y,x=que.popleft()
        print(str(cost)+' '+str(direction)+' '+str(y)+' '+str(x))
        
        if y==(boardSize-1) and x==(boardSize-1):
            if answer>cost:
                answer=cost
            continue
        visited[y][x]=True
        print(visited)
        for i in range(len(UDLR)):
            dx=x+UDLR[i][1]
            dy=y+UDLR[i][0]
            
            
            if dx<0 or dx>=boardSize or dy<0 or dy>=boardSize:
                continue
            if board[dy][dx]==1:
                continue
            if visited[dy][dx]:
                continue
            
            nextCost=0
            if direction!=i:
                nextCost=600
            else:
                nextCost=100
            que.append((cost+nextCost,i,dy,dx))
            
        
        
    return answer
graph=[[0,0,0],[0,0,0],[0,0,0]]

print(solution(graph))