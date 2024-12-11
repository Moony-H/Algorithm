def sliceByNumber(string):
    result=[]
    i=0
    while i<len(string):
        c=string[i]
        asc=ord(c)
        if asc >= ord('0') and asc<=ord('9'):
            if asc == ord('1') and ord(string[i+1]) == ord('0'):
                result.append([10])
                i+=1
            else:
                result.append([asc-ord('0')])
        else:
             result[-1].append(c)        
        i+=1
    return result
    


def solution(dartResult):
    answer = 0
    dartResults=sliceByNumber(dartResult)
    points=[0 for _ in range(len(dartResults))]
    
    for i in range(len(dartResults)):
        p=dartResults[i][0]
        area=dartResults[i][1]
        if area=='D':
            p=p**2
        elif area=='T':
            p=p**3
        if len(dartResults[i])==3:
            option=dartResults[i][2]
            if option=="*":
                p=p*2
                if i!=0:
                    points[i-1]=points[i-1]*2
            else:
                p=-p
        points[i]=p
        
    return sum(points)