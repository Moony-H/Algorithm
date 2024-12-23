def find(start,dic,msg,num):
    result=0
    for i in range(len(msg)-start):
        c= msg[start:start+i+1]
        if c in dic:
            result=dic[c]
        else:
            dic[c]=num
            return (result,i)
    return (result,len(msg)-start)

def solution(msg):
    answer = []
    dic={chr(i+ord('A')):i+1 for i in range(0,26)}
    num=27
    i=0
    while i<len(msg):
        result=find(i,dic,msg,num)
        num+=1
        answer.append(result[0])
        i+=result[1]
        
                
    return answer