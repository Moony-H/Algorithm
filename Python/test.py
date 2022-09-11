import sys

input=sys.stdin.readline

answers=[]

    

L,_=map(int,input().rstrip().split())

alpha=input().rstrip().split()

alpha.sort()
def aeiou(s):
    answer=0
    for i in ['a','e','i','o','u']:
        answer+=s.count(i)
    return answer
def dfs(s,depth,index,array,length):
    global answers
    if(depth==0 and len(s)==length):
        num=aeiou(s)
        if(num>=1 and len(s)-num>=2):
            answers.append(s)
    for i in range(index,len(array)):
        dfs(s,depth-1,i+1,array,length)
        dfs(s+array[i],depth-1,i+1,array,length)

dfs('',L,0,alpha,L)
for i in answers:
    print(i)


