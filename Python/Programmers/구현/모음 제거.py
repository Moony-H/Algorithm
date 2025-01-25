def solution(s):
    return ''.join(['' if i in ['a','e','i','o','u'] else i for i in s])