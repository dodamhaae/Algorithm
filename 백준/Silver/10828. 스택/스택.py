import sys

stack=[]
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    if 'push' in s:
        stack.append(s.split()[1])
    elif s == 'pop':
        print(stack[-1] if stack else -1)
        stack = stack[:-1]
    elif s == 'size':
        print(len(stack))
    elif s == 'empty':
        print(0 if stack else 1)
    elif s == 'top':
        print(stack[-1] if stack else -1)