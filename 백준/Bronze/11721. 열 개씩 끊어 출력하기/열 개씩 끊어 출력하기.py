import sys

N = [x for x in sys.stdin.readline().strip()]
for i in range(0,len(N),10):
    print(''.join(N[i:i+10]))