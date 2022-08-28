import sys
input=sys.stdin.readline

def fib(n):

    if(n==1 or n==2):
        return 1
    return fib(n-1)+fib(n-2)

dp=[-1]*41
dp[1]=1
dp[2]=1
count=0

def fib2(n):
    global count
    if(dp[n]==-1):
        dp[n]=fib2(n-1)+fib2(n-2)
        count+=1
    return dp[n]
    


n=int(input().rstrip())
print(fib(n))
fib2(n)
print(count)

