import sys

def facto(a):
    result=1
    for i in range(a):
        result=result*(i+1)
    return result


def solution(n,m):
    return facto(m) // (facto(n) * facto(m - n))
    

input=sys.stdin.readline

case=int(input())
for i in range(case):
    n,m=map(int,input().rstrip().split())
    print(solution(n,m))
