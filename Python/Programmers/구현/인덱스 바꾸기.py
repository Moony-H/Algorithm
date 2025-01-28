def solution(s, n1, n2):
        return ''.join([s[n2] if i==n1 else( s[n1] if i==n2 else s[i]) for i in range(len(s))])