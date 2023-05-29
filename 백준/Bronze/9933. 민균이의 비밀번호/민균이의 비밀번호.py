import sys

password = [sys.stdin.readline().strip() for _ in range(int(sys.stdin.readline()))]
for p in password:
    if p[::-1] in password or p==p[::-1]:
        print(len(p), p[len(p)//2])
        break