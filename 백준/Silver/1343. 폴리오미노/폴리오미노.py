import sys

P = sys.stdin.readline()
P = P.replace('XXXX','AAAA').replace('XX','BB')
print(-1 if 'X' in P else P)