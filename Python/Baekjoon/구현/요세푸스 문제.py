import sys

input=sys.stdin.readline

n,k=map(int,input().split())
index=0
answers=[]
arr=[i+1 for i in range(n)]
while len(arr)!=0:
    index+=k-1
    if index>=len(arr):
        index%=len(arr)
    answers.append(arr[index])
    del arr[index]

print("<",end="")

for i in range(len(answers)):
    if i==len(answers)-1:
        print(answers[i], end=">")
        continue
    print(answers[i], end=", ")
    
