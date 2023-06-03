import sys

Caesar = sys.stdin.readline().strip()
JOI = []
for c in Caesar:
    JOI.append(chr(ord(c)-3+26)) if c < 'D' else JOI.append(chr(ord(c)-3))
print(''.join(JOI))