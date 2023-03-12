def solution(num, k):
    n = [int(x) for x in str(num)]
    return n.index(k)+1 if k in n else -1