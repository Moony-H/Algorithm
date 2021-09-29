from collections import deque

def algorithm(a):
    que=deque()
    que.append([0,0])
    dir=[[1,0],[1,1]]
    length=len(a)


    while que:
        temp=que.popleft()
        y=temp[0]+1
        x=temp[1]
        print(str(y-1)+','+str(x))
        if y>=length:
            print('len')
            continue
        if a[y][x]==-1 and a[y][x+1]==-1:
            que.append([temp[0],temp[1]])

        elif a[y][x]!=-1:
            a[y][x+1]=a[temp[0]][temp[1]]-a[y][x]
            que.append([y,x])
            que.append([y,x+1])
            continue

        elif a[y][x+1]!=-1:
            a[y][x]=a[temp[0]][temp[1]]-a[y][x+1]
            que.append([y,x])
            que.append([y,x+1])
            continue
            



a=[[20],[5,-1],[-1,-1,12],[-1,-1,2,-1],[1,-1,-1,-1,-1]]
algorithm(a)

print(a)