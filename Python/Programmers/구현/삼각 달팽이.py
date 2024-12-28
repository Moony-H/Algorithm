def down(arr,p,n,repeat):
    for i in range(repeat):
        arr[p[1]+i][p[0]]=n
        n+=1
    return (p[0]+1,p[1]+repeat-1)
def right(arr,p,n,repeat):
    for i in range(repeat):
        arr[p[1]][p[0]+i]=n
        n+=1
    return (p[0]+repeat-2,p[1]-1)

def upLeft(arr,p,n,repeat):
    for i in range(repeat):
        arr[p[1]-i][p[0]-i]=n
        n+=1
    return (p[0]-repeat+1,p[1]-repeat+2)

def solution(n):
    answer = []
    arr=[[0 for _ in range(i+1)]for i in range(n)]
    functions=[down, right, upLeft]
    number=1
    p=(0,0)
    for i in range(n):
        fun=functions[i%3]
        p=fun(arr,p,number,n-i)
        number+=n-i
    for i in arr:
        answer+=i
        
    return answer