
import sys

input=sys.stdin.readline

n=int(input().rstrip())

arr=list(map(int,input().rstrip().split()))

answer=0

def calc(arr):
    result=0
    for i in range(len(arr)-1):
        result+=abs(arr[i]-arr[i+1])
    return result

def pick(choice,picked,arr):
    global answer
    if(len(picked)==len(arr)):
        answer=max(answer,calc(picked))
    for i in range(len(arr)):
        if i in choice:
            continue
        choice.append(i)
        picked.append(arr[i])
        pick(choice,picked,arr)
        choice.pop()
        picked.pop()

pick([],[],arr)

print(answer)
