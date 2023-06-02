import sys

S = sys.stdin.readline().strip()
for v in ['a','e','i','o','u']:
    S = S.replace(v+'p'+v, v)
print(S)