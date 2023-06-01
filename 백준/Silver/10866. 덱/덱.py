import sys

deque=[]
for _ in range(int(sys.stdin.readline())):
    d = sys.stdin.readline().strip()
    if 'push_front' in d:
        deque.insert(0,d.split()[1])
    elif 'push_back' in d:
        deque.append(d.split()[1])
    elif 'pop_front' in d:
        print(deque[0] if deque else -1)
        deque = deque[1:]
    elif 'pop_back' in d:
        print(deque[-1] if deque else -1)
        deque = deque[:-1]
    elif d == 'size':
        print(len(deque))
    elif d == 'empty':
        print(0 if deque else 1)
    elif d == 'front':
        print(deque[0] if deque else -1)
    elif d == 'back':
        print(deque[-1] if deque else -1)