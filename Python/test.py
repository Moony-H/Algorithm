
import sys

input=sys.stdin.readline

table=[[0 for _ in range(100)] for _ in range(100)]

n=int(input().rstrip())

for _ in range(n):
    x,y=map(int,input().rstrip().split())
    for i in range(x,x+10):
        for j in range(99-y-10,99-y):
            table[i][j]=1
    

answer=0

for i in table:
    for j in i:
        answer+=j

print(answer)