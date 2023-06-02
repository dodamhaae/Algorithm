import sys

print(''.join([x for x in sys.stdin.readline().strip() if x not in ['C','A','M','B','R','I','D','G','E']]))
