import sys

for i in range(int(sys.stdin.readline())):
    print(f'Case #{i+1}:', ' '.join(sys.stdin.readline().split()[::-1]))