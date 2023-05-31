import sys

N, M = sys.stdin.readline().split()
n = {sys.stdin.readline().strip() for _ in range(int(N))}
m = {sys.stdin.readline().strip() for _ in range(int(M))}

p=[]
for x in m:
    if x in n:
        p.append(x)
print(len(p))

for x in sorted(p):
    print(x)