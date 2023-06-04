import sys

N = int(sys.stdin.readline())
n = [int(x) for x in sys.stdin.readline().split()]
print(min(n), max(n))