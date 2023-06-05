import sys

N = int(sys.stdin.readline())
C = [[c for c in map(int,sys.stdin.readline().split())] for _ in range(N)]
for c in sorted(C):
    print(c[0], c[1])