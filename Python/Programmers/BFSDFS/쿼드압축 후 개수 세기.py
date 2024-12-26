def isSame(table,start,end):
    n=table[start[1]][start[0]]
    for i in range(start[1],end[1]):
        for j in range(start[0],end[0]):
            if table[i][j]!=n:
                return False
    return True

def compress(table,start,end):
    result=[0,0]
    if isSame(table,start,end):
        result[table[start[1]][start[0]]]+=1
        return result
    lx=end[0]-start[0]
    ly=end[1]-start[1]
    a=compress(table,start,(end[0]-lx//2,end[1]-ly//2))
    b=compress(table,(start[0]+lx//2,start[1]),(end[0],end[1]-ly//2))
    c=compress(table,(start[0],start[1]+ly//2),(end[0]-lx//2,end[1]))
    d=compress(table,(start[0]+lx//2,start[1]+ly//2),end)
    return [a[0]+b[0]+c[0]+d[0],a[1]+b[1]+c[1]+d[1]]
            
    

def solution(arr):
    return compress(arr,(0,0),(len(arr),len(arr)))