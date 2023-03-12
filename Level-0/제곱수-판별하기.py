def solution(n):
    for i in range(n//2):
        if i*i == n:
            return 1
    return 2