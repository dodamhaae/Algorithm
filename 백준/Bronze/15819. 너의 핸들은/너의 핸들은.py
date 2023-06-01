import sys

N, I = sys.stdin.readline().split()
handle=[]
for _ in range(int(N)):
    h = sys.stdin.readline().strip()
    handle.append(h)
print(sorted(handle)[int(I)-1])