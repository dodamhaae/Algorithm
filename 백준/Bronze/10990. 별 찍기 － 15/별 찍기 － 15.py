import sys

N = int(sys.stdin.readline())
print(' '*(N-1) + '*')
for n in range(1,N):
    print(' '*(N-n-1) + '*' + ' '*(n*2-1) + '*')