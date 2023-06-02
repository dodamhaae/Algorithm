import sys

for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline()
    total = int(n) + int(n[::-1])
    print('YES'if str(total) == str(total)[::-1] else 'NO')