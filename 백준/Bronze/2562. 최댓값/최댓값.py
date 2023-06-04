import sys

N = {int(sys.stdin.readline()): i+1 for i in range(9)}
print(max(N))
print(N.get(max(N)))