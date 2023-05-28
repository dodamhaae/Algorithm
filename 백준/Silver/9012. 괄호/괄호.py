import sys

n = int(sys.stdin.readline())
for _ in range(n):
    v = sys.stdin.readline().rstrip()
    while '()' in v:
        v = v.replace('()','')
    print('NO' if len(v) else 'YES')