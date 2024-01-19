def strToMinute(timeString):
    h,m=map(int,timeString.split(':'))
    return 60*h+m

def solution(book_time):
    answer = 0
    timeRange=[0 for _ in range(1440)]
    for i in book_time:
        start,end=map(strToMinute,i)
        end+=10
        if(end>1439):
            end=1439
        for j in range(start,end):
            timeRange[j]+=1
    return max(timeRange)