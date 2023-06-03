import sys

N = int(sys.stdin.readline())
for i in range(N):
    print('* '*N if i%2==0 else ' *'*N)