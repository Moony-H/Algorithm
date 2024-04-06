from collections import deque

def stringToMinute(time):
    timeList=time.split(":")
    return int(timeList[0])*60+int(timeList[1])
    

def solution(plans):
    answer = []
    plans=[[i[0],stringToMinute(i[1]),int(i[2])] for i in plans]
    plans.sort(key= lambda x:x[1])
    stack=[]
    
    for i in range(len(plans)):

        name,startTime,time=plans[i]
        if(i==len(plans)-1):
            #마지막
            answer.append(name)
            continue
        nName,nStartTime,nTime=plans[i+1]
        timeInterval=nStartTime-startTime
        if timeInterval>=time:
            #그냥 제시간에 끝남
            answer.append(name)
            remainTime=timeInterval-time
            while remainTime>0 and len(stack)>0:
                #전에 안해놨던거 있음
                stackTime=stack[-1][1]
                stack[-1][1]-=remainTime
                remainTime-=stackTime
                if(stack[-1][1]<=0):
                    popedName,_=stack.pop()
                    answer.append(popedName)
        else:
            #제시간에 못끝냄.
            stack.append([name,time-timeInterval])
    
    for _ in range(len(stack)):
        name,_=stack.pop()
        answer.append(name)
                
        
    
    return answer