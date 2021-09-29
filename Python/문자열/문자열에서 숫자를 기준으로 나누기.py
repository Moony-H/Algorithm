from itertools import combinations

import re

a='100*3-200'

b=re.split('(\d+)',a)[1:-1]
print(b)