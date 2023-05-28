from itertools import combinations
def solution(number):
    return [sum(n) for n in combinations(number,3)].count(0)