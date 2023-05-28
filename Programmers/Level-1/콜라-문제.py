def solution(a, b, n):
    answer=0
    while n>=a:
        cola = n//a*b
        n = cola + n%a
        answer+=cola
    return answer