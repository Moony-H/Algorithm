from heapq import heappop, heappush
import sys

_,num=map(int,input().split())

arr=list(map(int,input().split()))

for i in range(1,len(arr)):
    arr[i]+=arr[i-1]

print(arr)
l=-1
r=num-1
answer=0
while r<len(arr):
    answer=max(answer,arr[r]-arr[l])
    print(arr[r]-arr[l])
    l+=1
    r+=1

print(answer)

