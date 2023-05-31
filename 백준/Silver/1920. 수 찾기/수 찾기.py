import sys

N = sys.stdin.readline()
A = set(sys.stdin.readline().split())
M = sys.stdin.readline()
for x in sys.stdin.readline().split():
    print(1 if x in A else 0)