def change(s,index,skip):
    aInt=ord('a')
    sInt=ord(s)-aInt
    limit=ord('z')-aInt+1
    i=0
    while(i<index):

        sInt=(sInt+1)%limit
        if(chr(sInt+aInt) in skip):
            continue
        i+=1
    return chr(sInt+ord('a'))

def solution(s, skip, index):
    answer = ''
    
    for i in s:
        answer+=change(i,index,skip)
    return answer