import sys
import heapq as hq

heap=[]
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x==0:
        print(hq.heappop(heap)[1] if heap else 0)
    else:
        hq.heappush(heap,(-x,x))