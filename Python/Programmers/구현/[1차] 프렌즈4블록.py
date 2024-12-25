
            

def down(table,line,m):
    for i in range(m-1,-1,-1):
        if table[i][line]=="":
            continue
        start=i
        while start+1<len(table) and table[start+1][line]=="":
            table[start+1][line]=table[start][line]
            table[start][line]=""
            start+=1

def cleanTable(table,m,n):
    for i in range(n):
        down(table,i,m)
def scanTable(table,m,n):
    nums=set()
    for i in range(m-1):
        for j in range(n-1):
            c=table[i][j]
            if c=="": continue
            if table[i+1][j] ==c and table[i][j+1]==c and table[i+1][j+1]==c:
                nums.add((i,j))
                nums.add((i+1,j))
                nums.add((i,j+1))
                nums.add((i+1,j+1))
    return nums
                

def solution(m, n, board):
    answer = 0
    table=list(map(list,board))
    while True:
        result=scanTable(table,m,n)
        answer+=len(result)
        if len(result)==0:
            break
        for i in result:
            table[i[0]][i[1]]=""
        cleanTable(table,m,n)
    return answer