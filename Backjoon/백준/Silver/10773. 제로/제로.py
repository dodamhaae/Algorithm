import sys

l=[]
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n==0:
        l=l[:-1]
    else:
        l.append(n)
print(sum(l))