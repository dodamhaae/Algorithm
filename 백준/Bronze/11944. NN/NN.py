import sys

N, M = map(int, sys.stdin.readline().split())
print((str(N)*N)[:M])