import sys

for _ in range(int(sys.stdin.readline())):
    S = [s[::-1] for s in sys.stdin.readline().strip().split()]
    print(' '.join(S))