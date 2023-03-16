def solution(x):
    return True if x%sum([int(x) for x in str(x)])==0 else False