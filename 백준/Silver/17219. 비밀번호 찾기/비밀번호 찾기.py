import sys

N, M = sys.stdin.readline().split()

k = {}
for _ in range(int(N)):
    p = sys.stdin.readline().split()
    k[p[0]] = p[1]

for _ in range(int(M)):
    s = sys.stdin.readline().strip()
    print(k.get(s))