def solution(n):
    for i in range(6, n*6+1, 6):
        if i % n == 0:
            return i/6