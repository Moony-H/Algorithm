import sys

input=sys.stdin.readline

INF=int(1e9)

n=int(input())
m=int(input())

table=[[INF for _ in range(n)]for _ in range(n)]


for i in range(n):
    for j in range(n):
        if i==j:
            table[i][j]=0

for _ in range(m):
    s,e,c=map(int,input().split())
    table[s-1][e-1]=min(table[s-1][e-1],c)



for i in range(n):
    for j in range(n):
        for k in range(n):
            table[j][k] = min(table[j][k], table[j][i] + table[i][k])


for i in table:
    for j in i:
        print(j if(j != INF) else 0,end=" ")
    print()