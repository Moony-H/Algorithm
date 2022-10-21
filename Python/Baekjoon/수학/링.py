import sys

def GDC(x,y):
    while(y):
        x,y=y,x%y
    return x

def calc(num1,num2):
    a=GDC(num1,num2)
    return str(num1//a)+"/"+str(num2//a)


input=sys.stdin.readline

n=int(input().rstrip())

arr=list(map(int,input().rstrip().split()))

for i in range(1,n):
    print(calc(arr[0],arr[i]))
