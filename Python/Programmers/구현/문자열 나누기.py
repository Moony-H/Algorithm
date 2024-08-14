import sys
sys.setrecursionlimit(1000000)

def find(s):
    if(len(s)==0):
        return 0
    fNum=0
    eNum=0
    index=-1
    for i,c in enumerate(s):
        print(str(fNum)+" "+str(eNum))
        if(c==s[0]):
            fNum+=1
        else:
            eNum+=1
        if(fNum==eNum):
            index=i
            break
    if(index==-1):
        index=len(s)-1
    return 1+find(s[index+1:])


def solution(s):
    answer = 0
    return find(s)
    return answer