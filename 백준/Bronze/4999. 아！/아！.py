import sys

J = sys.stdin.readline().strip()
D = sys.stdin.readline().strip()
print('go' if J.count('a') >= D.count('a') else 'no')