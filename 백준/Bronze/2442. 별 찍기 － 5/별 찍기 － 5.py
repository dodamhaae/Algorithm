import sys

N = int(sys.stdin.readline())
for i in range(N):
    print(' '*(N-i-1)+'*'*(2*i+1))