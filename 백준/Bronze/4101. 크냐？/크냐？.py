import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A==0 & B==0:
        break
    print('Yes' if A > B else 'No')