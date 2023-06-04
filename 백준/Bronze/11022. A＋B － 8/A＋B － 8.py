import sys

for i in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {A} + {B} = {A+B}')