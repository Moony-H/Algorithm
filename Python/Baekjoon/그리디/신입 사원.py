import sys
from itertools import permutations
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    participant=[]
    answer=0
    for _ in range(n):
        participant.append(list(map(int,input().split())))
    participant.sort(key= lambda x:x[0])
    m=100001
    for i in participant:
        m=min(i[1],m)
        if m<i[1]:
            answer+=1
    print(n-answer)
