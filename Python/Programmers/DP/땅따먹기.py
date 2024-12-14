def m(line,skip):
    result=0
    for i in range(len(line)):
        if i==skip: continue
        result= result if result>=line[i] else line[i]
    return result
    

def solution(land):
    
    for i in range(1,len(land)):
        for j in range(4):
            maxNum=m(land[i-1],j)
            land[i][j]+=maxNum
    
    return max(land[-1])