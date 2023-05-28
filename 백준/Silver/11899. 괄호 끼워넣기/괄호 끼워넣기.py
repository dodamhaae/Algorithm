import sys

b = sys.stdin.readline().strip()
while '()' in b:
    b = b.replace('()','')
print(len(b))