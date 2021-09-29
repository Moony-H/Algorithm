

def printStar(y,x,plus):
    global array
    if plus==1:
        array[y][x]='*'
        return
    plus//=3


    for i in range(3):
        printStar(y,x+(plus*i),plus)

    printStar(y+(plus*1),x,plus)
    printStar(y+(plus*1),x+(plus*2),plus)

    for i in range(3):
        printStar(y+(plus*2),x+(plus*i),plus)





n=int(input())

array=[[' ' for _ in range(n) ]for _ in range(n)]

printStar(0,0,n)

for i in range(n):
    for j in range(n):
        print(array[i][j],end='')
    print()
    
