def repeat(string):
    num=0
    newString=''
    for i in range(len(string)):
    
            
        if string[i]!='.' and num>=1:
            num=0
            newString+='.'
            newString+=string[i]
            
        elif string[i]!='.':
            newString+=string[i]
            
        if string[i]=='.':
            num+=1
    return newString
            



def solution(new_id):
    answer = ''
    first=new_id.lower()
    second=''
    for i in range(len(first)):
        if first[i]=='-' or first[i]=='_' or first[i]=='.' or (first[i].isalpha()) or (first[i].isdigit()):
            second+=first[i]
    third=repeat(second)
    fourth=''
    if len(third)>0:
        if third[0]=='.':
            third=third[1:]
        if third[-1]=='.':
            third=third[0:-1]
    fourth=third
    
    fifth=fourth
    print(fifth)
    if fifth=='':
        fifth+='a'
    sixth=''

    if len(fifth)>=16:
        sixth=fifth[0:15]
        if sixth[-1]=='.':
            sixth=sixth[0:-1]
    else:
        sixth=fifth
    if len(sixth)<3:
        while True:
            if len(sixth)>=3:
                break
            sixth=sixth+sixth[-1]

    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)
    print(sixth)
    
    answer=sixth

    
    return answer
string="=.="


print(solution(string))