
answer=0
isEnd=False
endX=0
endY=0
def solution(x,y,n,score):
    global answer
    global endX
    global endY
    new=n//2
    if endX==x and endY==y:
        answer=score
        return
    if endX<x+new and endX>=0 and endY<y+new and endY>=0:
        solution(x,y,new,score)
    elif endX>=x+new and endX<n and endY<y+new and endY>=0:
        score+=new**2
        solution(x+new,y,new,score)
    elif endX<x+new and endX>=0 and endY>=y+new and endY<n:
        score+=(new**2)*2
        solution(x,y+new,new,score)
    else:
        score+=(new**2)*3
        solution(x+new,y+new,new,score)


n,endY,endX=map(int,input().split())

n=2**n
solution(0,0,n,0)

print(answer)