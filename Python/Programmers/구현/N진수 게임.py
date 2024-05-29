from collections import deque

#10이 넘어가는 숫자이면 맞는 기호로 바꾼다.
def changeToCharNum(num):
    arr=['A','B','C','D','E','F']
    return str(num) if num<10 else arr[num-10]

#위의 함수를 이용하여 문자열 리스트를 만든다.
def getChangedStringList(numbers):
    temp=['']*len(numbers)
    for i in range(len(numbers)):
        temp[i]=changeToCharNum(numbers[i])
    return temp

#N진수 시스템을 만든다. nextNum을 호출할 때 마다 다음 진수를 출력한다.
#2진수 예) [0] -> [1] -> [1,0] -> [1,1] -> [1,0,0] -> [1,0,1] ...
#7진수 예) [0] -> [1] -> [2] -> ... -> [6] -> [1,0] -> [1,1] -> [1,2] ...
def nextNum(numbers,numType):
    if len(numbers)==0:
        numbers.append(0)
        return
    upValue=1
    for i in range(len(numbers)-1,-1,-1):
        if upValue==0:
            return
        numbers[i]+=upValue
        upValue=0
        if numbers[i]>=numType:
            upValue=1
            numbers[i]=0
    if upValue!=0:
        numbers.appendleft(1)
    return
        
        

def solution(n, t, m, p):
    #정답
    answer = ''
    #앞쪽 데이터 추가의 효율성과 코드 가독성을 위해 deque 사용
    q=deque()
    #t*m의 길이를 넘는(대답할 숫자들이 모두 포함된)문자열 저장
    s=''
    
    #s 구하기
    while len(s)<t*m:
        nextNum(q,n)
        stringList=getChangedStringList(q)
        s+=''.join(stringList)
    
    #대답할 문자 구하기
    i=0
    while len(answer)<t:
        #현재 문자
        c=s[i]
        #자신의 차례라면 대답하기
        if(p-1)==i%m:
            answer+=c
        i+=1
    return answer