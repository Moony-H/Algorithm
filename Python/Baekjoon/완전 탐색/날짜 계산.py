
import sys

input=sys.stdin.readline

e,s,m=map(int,input().rstrip().split())

#15,28,19
num=1
E,S,M=1,1,1
while True:
    if(E==e and S==s and M==m):
        print(num)
        exit(0)
    E+=1
    S+=1
    M+=1
    if(E>15):
        E=1
    if(S>28):
        S=1
    if(M>19):
        M=1
    num+=1


