import sys
input=sys.stdin.readline

_,m=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(1,len(arr)):
    arr[i]=arr[i]+arr[i-1]
for _ in range(m):
    i,j=map(int,input().split())
    i-=2
    j-=1
    if(i<0):
        print(arr[j])
    else:
        print(arr[j]-arr[i])
