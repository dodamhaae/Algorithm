import sys

N, M = sys.stdin.readline().split()
for _ in range(int(N)):
    print(sys.stdin.readline().strip()[::-1])