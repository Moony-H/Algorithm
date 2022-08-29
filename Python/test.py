import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    a,b=map(int,input().split())
    num=a**b
    num%=10
    print(num)
