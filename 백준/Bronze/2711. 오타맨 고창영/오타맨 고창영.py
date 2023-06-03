import sys

for _ in range(int(sys.stdin.readline())):
    N, S = sys.stdin.readline().split()
    print(''.join([S[x] for x in range(len(S)) if not x==int(N)-1]))