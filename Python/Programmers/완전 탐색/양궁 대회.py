apeach=[]
maximum=0
answer=[]
def point(a,b):
    resultA=0
    resultB=0
    for i in range(11):
        if a[i]==0 and b[i]==0:
            continue
        if a[i]>b[i]:
            resultA+=(10-i)
        else:
            resultB+=(10-i)
    return resultA-resultB

def recur(depth,n,result):
    global maximum
    global apeach
    global answer
    if depth==1:
        result.append(n)
        diff=point(list(reversed(result)),apeach)
        
        if diff>maximum:
            maximum=diff
            answer=list(reversed(result))
        del result[-1]
        return
    for i in range(n,-1,-1):
        result.append(i)
        recur(depth-1,n-i,result)
        del result[-1]

def solution(n, info):
    global apeach
    global maximum
    apeach=info
    arr=[1,2,3]
    global answer
    recur(11,n,[])
    if answer==[]:
        answer=[-1]
    return answer