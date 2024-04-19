import sys
sys.setrecursionlimit(1000000)

UDLR=[[0,-1],[0,1],[-1,0],[1,0]]

def dfs(position,table):
    x,y=position
    answer=0
    answer+=table[y][x]
    table[y][x]=0
    for i in UDLR:
        dx=x+i[0]
        dy=y+i[1]
        if dx<0 or dx>=len(table[0]) or dy<0 or dy>=len(table):
            continue
        if table[dy][dx]=='X' or table[dy][dx]==0:
            continue
        answer+=dfs((dx,dy),table)
    return answer


def solution(maps):
    answer = []
    newMap=[[int(j) if j.isdecimal() else j for j in i] for i in maps]
    for i in range(len(newMap)):
        for j in range(len(newMap[i])):
            if newMap[i][j]=='X' or newMap[i][j]==0:
                continue
            answer.append(dfs((j,i),newMap))
    return sorted(answer) if len(answer)!=0 else [-1]