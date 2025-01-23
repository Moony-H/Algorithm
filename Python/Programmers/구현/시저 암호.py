def up(a,n):
    return chr(((ord(a)-ord('A')+n)%(ord('Z')-ord('A')+1))+ord('A'))
def low(a,n):
    return chr(((ord(a)-ord('a')+n)%(ord('z')-ord('a')+1))+ord('a'))
def change(a,n):
    return up(a,n) if ord('A')<=ord(a)<=ord('Z') else low(a,n)

def solution(s, n):
    return ''.join([i if i==' ' else change(i,n) for i in s])