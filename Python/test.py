from heapq import heappop, heappush
import sys
input=sys.stdin.readline
_,num=map(int,input().split())

arr=list(map(int,input().split()))

for i in range(1,len(arr)):
    arr[i]+=arr[i-1]

l=-1
r=num-1
answer=-999999999
while r<len(arr):
    if(l==-1):
        answer=max(answer,arr[r])
        l+=1
        r+=1
        continue
    answer=max(answer,arr[r]-arr[l])
    l+=1
    r+=1

print(answer)

