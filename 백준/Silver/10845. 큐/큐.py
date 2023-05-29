import sys

queue=[]
for _ in range(int(sys.stdin.readline())):
    q = sys.stdin.readline().strip()
    if 'push' in q:
        queue.append(q.split()[1])
    elif q=='pop':
        print(queue[0] if queue else -1)
        queue = queue[1:]
    elif q=='size':
        print(len(queue))
    elif q=='empty':
        print(0 if queue else 1)
    elif q=='front':
        print(queue[0] if queue else -1)
    elif q=='back':
        print(queue[-1] if queue else -1)