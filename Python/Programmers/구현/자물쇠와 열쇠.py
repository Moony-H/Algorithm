def isCollect(x,y,lockLength,graph):
    for i in range(lockLength):
        for j in range(lockLength):
            if graph[x+i][y+j]==0 or graph[x+i][y+j]>1:
                return False
    return True
        
def printer(graph):
    for i in graph:
        print(i)

def attach(x,y,key,graph):
    result=graph
    for i in range(len(key)):
        for j in range(len(key)):
            result[x+i][y+j]+=key[i][j]
    return result

def dettach(x,y,key,graph):
    result=graph
    for i in range(len(key)):
        for j in range(len(key)):
            result[x+i][y+j]-=key[i][j]
    return result
    

def rotate(a):
    n = len(a)
    m = len(a[0])
    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    
    return result

def solution(key, lock):
    answer=False
    
    height=len(key)*2+len(lock)-2
    graph=[[0 for _ in range(height)]for _ in range(height)]
    
    lockStartX=len(key)-1
    lockStartY=lockStartX
    
    for i in range(len(lock)):
        for j in range(len(lock)):
            graph[i+len(key)-1][j+len(key)-1]=lock[i][j]
    for i in range(4):
        key=rotate(key)
        printer(key)
        print()
    for i in range(4):
        key=rotate(key)
        
        for j in range(len(key)-1+len(lock)):
            for k in range(len(key)-1+len(lock)):
                result=attach(j,k,key,graph)
                
                if(isCollect(lockStartX,lockStartY,len(lock),result)):
                    return True
                result=dettach(j,k,key,graph)
    
    
    
        
    return False