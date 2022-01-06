def repeat(string):
    num=0
    newstring=''
    for i in range(len(string)):
    
            
        if string[i]!='.' and num>=1:
            num=0
            newstring+='.'
            newstring+=string[i]
            
        elif string[i]!='.':
            newstring+=string[i]
            
        if string[i]=='.':
            num+=1
    return newstring