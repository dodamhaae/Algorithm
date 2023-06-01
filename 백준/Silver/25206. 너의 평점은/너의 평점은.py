import sys

p,total=0,[]
grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
for _ in range(20):
    n, s, g = sys.stdin.readline().split()
    if not g == 'P':
        p += float(s)
        total.append(float(s)*grade.get(g))
print(f'{sum(total)/p:.6f}')