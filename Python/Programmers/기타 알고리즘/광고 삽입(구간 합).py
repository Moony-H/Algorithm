def stringToSeconds(time):
    l=list(map(int,time.split(":")))
    l[0]=l[0]*3600
    l[1]=l[1]*60
    return sum(l)


def secondsToTime(sec):
    h=sec//3600
    sec%=3600
    m=sec//60
    sec%=60
    h=str(h) if h>=10 else '0'+str(h)
    m=str(m) if m>=10 else '0'+str(m)
    sec=str(sec) if sec>=10 else '0'+str(sec)
    return str(h)+":"+str(m)+":"+str(sec)


def solution(play_time, adv_time, logs):
    answer = ''
    allTime=[0]*(stringToSeconds(play_time)+1)
    
    for i in logs:
        s,e=i.split('-')
        allTime[stringToSeconds(s)]+=1
        allTime[stringToSeconds(e)]-=1
    for i in range(0,len(allTime)-1):
        allTime[i+1]+=allTime[i]
    
    
    
    adv=stringToSeconds(adv_time)
    temp=sum(allTime[:adv])
    result=temp
    start=0
    for i in range(1,len(allTime)-adv+1):
        temp-=allTime[i-1]
        temp+=allTime[i+adv-1]

        if result<temp:
            result=temp
            start=i

    answer=secondsToTime(start)
    return answer