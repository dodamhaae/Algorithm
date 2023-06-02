import sys

while True:
    A = sys.stdin.readline().strip()
    if A=='#':
        break
    a, s = A[0], A[2:].lower()
    print(a, s.count(a))