s = input()
new_s = s.split('-')
if len(new_s) == 1:
    print(sum([int(i) for i in s.split('+')]))
    exit(0)
print(sum([int(i) for i in new_s[0].split('+')])
      - sum([int(i) for i in ('+'.join(new_s[1:])).split('+')]))
