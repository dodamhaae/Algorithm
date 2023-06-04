import sys

N, X = map(int, sys.stdin.readline().split())
print(' '.join([a for a in sys.stdin.readline().split() if int(a)<X]))