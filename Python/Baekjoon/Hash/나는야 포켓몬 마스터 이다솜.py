import sys
input=sys.stdin.readline

n,m=map(int,input().split())
pokemon={}
for i in range(n):

    name=input().strip()
    pokemon[name]=str(i+1)
    pokemon[str(i+1)]=name
for _ in range(m):
    s=input().strip()
    print(pokemon[s])