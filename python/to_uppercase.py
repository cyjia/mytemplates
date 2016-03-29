import sys
import re

'''
replace (name = "M_messagecode") with (name = "M_MESSAGECODE")
'''

prog = re.compile(".*(M_.*)\"\).*")
for line in sys.stdin:
    m = prog.match(line.strip())
    if m and m.lastindex > 0:
        print(m.group().replace(m.group(1), m.group(1).upper()))
    else:
        print(line.strip())
