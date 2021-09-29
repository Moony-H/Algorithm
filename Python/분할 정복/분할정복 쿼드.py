m=int(input())
array=[]
for i in range(m):
    array.append(list(map(int,input())))

num=0

def quad(y,x,m):
    global num
    num+=1
    global array
    temp=array[y][x]
    breakPoint=False
    for i in range(y,y+m):
        for j in range(x,x+m):
            if temp!=array[i][j]:
                breakPoint=True
                break
        if breakPoint:
            break
    if breakPoint:
        end=m//2
        return '('+quad(y,x,end)+quad(y,x+end,end)+quad(y+end,x,end)+quad(y+end,x+end,end)+')'
        
    else:
        #if num==1:
        #    return '('+str(temp)+')'
        return str(temp)



print(quad(0,0,m))