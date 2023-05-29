import sys

cnt,day=0,0
N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()
for b in S:
    cnt+=1 if b=='(' else -1
    if abs(cnt)>day:
        day = abs(cnt)
print(-1 if abs(cnt)>0 else day)
