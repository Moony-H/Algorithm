import sys

input=sys.stdin.readline
sys.setrecursionlimit(10000)
flower=[[0,0],[-1,0],[0,-1],[1,0],[0,1]]
answer=int(1e9)
def dfs(table,costTable,cost,depth):
    global answer
    if depth==0:
        answer=min(answer,cost)
        return
    for y in range(len(table)):
        for x in range(len(table)):
            empty=[]
            for i in flower:
                dx=x+i[1]
                dy=y+i[0]
                if dx<0 or dx>=len(table) or dy<0 or dy>=len(table):
                    continue
                if table[dy][dx]==-1:
                    continue
                empty.append((dy,dx))
                
            if len(empty)<5:
                continue
            n=cost
            for i in empty:
                n+=costTable[i[0]][i[1]]
                table[i[0]][i[1]]=-1
            
            dfs(table,costTable,n,depth-1)
            for i in empty:
                table[i[0]][i[1]]=0
        
            
n=int(input())

table=[[0 for _ in range(n)]for _ in range(n)]
costTable=[]

for i in range(n):
    costTable.append(list(map(int,input().split())))
    
dfs(table,costTable,0,3)

print(answer)