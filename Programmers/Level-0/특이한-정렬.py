def solution(numlist, n):
    return [i[0] for i in sorted([(i,abs(n-i)) for i in sorted(numlist)][::-1], key=lambda x: x[1])]