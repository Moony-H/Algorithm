
import sys

input=sys.stdin.readline

n=int(input().rstrip())
mask=0
for i in range(n):
    temp=list(input().rstrip().split())
    if len(temp)==1:
        if temp[0]=='all':
            mask=0b111111111111111111111
            print(mask)
        else:
            mask=0
    else:
        num=int(temp[1])
        cmd=temp[0]
        if(cmd=='add'):
            mask=mask&1<<num

        elif cmd=='remove':
            mask=mask&~(1<<num)
        elif cmd=='check':
            if((mask&1<<num)):
                print(1)
            else:
                print(0)

        elif cmd=='toggle':
            if(mask&1<<num):
                mask=mask&~(1<<num)
            else:
                mask=mask&1<<num

   


