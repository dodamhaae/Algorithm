import sys

total = {str(n):'0' for n in range(10)}
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
N = [x for x in str(A*B*C)]
for n in set(N):
    total[n] = str(N.count(n))
print('\n'.join(list(total.values())))