import sys

DOW = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
Month = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
         '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
M, D = map(int, sys.stdin.readline().split())
m = 0
for i in range(1, M):
    m += Month.get(str(i))
print(DOW[(m+D)%7-1])