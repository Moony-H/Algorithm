import heapq
import sys

input=sys.stdin.readline


q=[]

n=int(input())
answer=[]
for _ in range(n):
    num=int(input())
    if num!=0:
        heapq.heappush(q,num)
        continue
    answer.append(0 if len(q)==0 else heapq.heappop(q))

for i in answer:
    print(i)