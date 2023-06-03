import sys

cnt=0
n = sorted(int(sys.stdin.readline()) for _ in range(28))
for i in range(1,31):
    if i not in n:
        print(i)
        cnt+=1
    if cnt == 2:
        break