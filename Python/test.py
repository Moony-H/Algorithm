
import sys

input=sys.stdin.readline

n=int(input().rstrip())
table=[]
for _ in range(n):
    table.append(list(map(int,input().rstrip().split())))

answer=0

def move(table,dir):
    temp=[[i for i in j]for j in table]
    if(dir==0):
        #왼쪽
        for i in range(len(temp)):
            for j in range(len(temp)-1):
                if temp[i][j]!=temp[i][j+1] and temp[i][j]!=0:
                    continue
                temp[i][j]+=temp[i][j+1]
                temp[i][j+1]=0
    if(dir==1):
        #오른쪽
        for i in range(len(temp)):
            for j in range(len(temp)-1,0,-1):
                if temp[i][j]!=temp[i][j-1] and temp[i][j]!=0:
                    continue
                temp[i][j]+=temp[i][j-1]
                temp[i][j-1]=0
    if(dir==2):
        #위
        for i in range(len(temp)):
            for j in range(len(temp)-1):
                if temp[j][i]!=temp[j+1][i] and temp[j][i]!=0:
                    continue
                temp[j][i]+=temp[j+1][i]
                temp[j+1][i]=0
    if(dir==3):
        #아래
        for i in range(len(temp)):
            for j in range(len(temp)-1,0,-1):
                if temp[j][i]!=temp[j-1][i] and temp[j][i]!=0:
                    continue
                temp[j][i]+=temp[j-1][i]
                temp[j-1][i]=0
    return temp


def find(table,num):

    global answer
    if num>=5:
        maximum=0
        for i in table:
            for j in i:
                maximum=max(maximum,j)
        answer=max(answer,maximum)
        return
    for i in range(4):
        find(move(table,i),num+1)




find(table,1)
print(answer)