import sys

N, k = map(int, sys.stdin.readline().split())
print((sorted([int(n) for n in sys.stdin.readline().split()])[::-1])[k-1])
