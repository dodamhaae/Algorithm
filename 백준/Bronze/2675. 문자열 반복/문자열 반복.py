import sys

for _ in range(int(sys.stdin.readline())):
    R, S = sys.stdin.readline().split()
    P = ''
    for s in S:
        P += s*int(R)
    print(P)