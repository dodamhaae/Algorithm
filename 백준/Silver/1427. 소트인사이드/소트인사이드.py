import sys

N = sys.stdin.readline().strip()
print(''.join(sorted([N[n] for n in range(len(N))])[::-1]))