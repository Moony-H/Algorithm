table=[[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]


def didWin(board):
    winCase=[[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
             [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
             [[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]
    for aP,bP,cP in winCase:
        a=board[aP[1]][aP[0]]
        b=board[bP[1]][bP[0]]
        c=board[cP[1]][cP[0]]
        if(a==b and b==c) and a!='.':
            return True
    return False
                        

def isSame(answer,board):
    for i in range(3):
        for j in range(3):
            if answer[i][j]!=board[i][j]:
                return False
    return True

def dfs(board,answer,iconNum):
    icons=['O','X']

    result=1
    if isSame(answer,board):
        return 0
    if didWin(board):
        return 1
    global table
    for x,y in table:
        if board[y][x]!='.':
            continue
        icon=icons[iconNum%2]
        board[y][x]=icon
        result*=dfs(board.copy(),answer,iconNum+1)
        board[y][x]='.'
    return result
        

def solution(board):
    newBoard=[[j for j in i] for i in board]
    emptyBoard=[['.','.','.'] for _ in range(3)]
    answer=dfs(emptyBoard,newBoard,0)
    #return 1
    
    return 1 if(answer==0) else 0