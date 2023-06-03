import sys

C = ''.join(sys.stdin.readline().split())
if C == '12345678':
    print('ascending')
elif C == '87654321':
    print('descending')
else:
    print('mixed')