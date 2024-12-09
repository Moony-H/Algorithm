import sys
input=sys.stdin.readline

N=int(input())
arr=[1 for _ in range(9)]
for _ in range(N):
    for i in range(1,len(arr)):
        arr[i]+=arr[i-1]

print(sum(arr))