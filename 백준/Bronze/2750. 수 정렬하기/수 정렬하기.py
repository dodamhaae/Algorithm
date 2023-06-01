import sys

N = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    N.append(n)
for n in sorted(N):
    print(n)