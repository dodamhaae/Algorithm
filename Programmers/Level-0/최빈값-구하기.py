def solution(array):
    cnt = [array.count(i) for i in set(array)]
    return -1 if cnt.count(max(cnt))>1 else list(set(array))[cnt.index(max(cnt))]