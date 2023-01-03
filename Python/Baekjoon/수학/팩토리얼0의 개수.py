
import sys

input=sys.stdin.readline

n=int(input().rstrip())
if(n==0):
    print(0)
    exit(0)
num=1
for i in range(2,n+1):
    num*=i

numString=str(num)
answer=0
for i in reversed(numString):
    if i=='0':
        answer+=1
    else:
        break
print(answer)