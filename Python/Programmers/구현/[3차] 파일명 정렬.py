def findNumber(string):
    start=-1
    end=len(string)
    ran=range(ord('0'),ord('9')+1)
    for i in range(len(string)):
        n=ord(string[i])
        if n in ran and start==-1:
            start=i
        elif n not in ran and start!=-1:
            end=i
            break
    return [string[:start],int(string[start:end]),string[end:]]
            

def solution(files):
    temp=[findNumber(files[i].upper())+[i] for i in range(len(files))]
    temp.sort(key=lambda x:(x[0],x[1],x[3]))
    
    answer = [ files[i[3]] for i in temp]
    
    return answer