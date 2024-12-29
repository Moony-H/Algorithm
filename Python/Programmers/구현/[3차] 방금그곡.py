def getCodes(string):
    stack=[]
    for i in string:
        if i=='#':
            stack[-1]+=i
            continue
        stack.append(i)
    return stack

def toMinute(timeString):
    h,m=map(int,timeString.split(':'))
    return h*60+m

def getMusicInfos(musics):
    infos=[]
    for i in musics:
        info=i.split(',')
        times=toMinute(info[1])-toMinute(info[0])
        codes=getCodes(info[3])
        cl=len(codes)
        resultCodes=(times//cl)*codes + codes[:(times%cl)]
        infos.append((info[2],resultCodes,times))
    return infos

def search(m,info):
    for i in range(len(info)-len(m)+1):
        temp=info[i:i+len(m)]
        if temp==m:
            return True
    return False

def solution(m, musics):
    answer = ''
    timeLen=0
    infos=getMusicInfos(musics)
    code=getCodes(m)
    for i in infos:
        if search(code,i[1]):
            if timeLen<i[2]:
                answer=i[0]
                timeLen=i[2]
    return answer if timeLen!=0 else '(None)'