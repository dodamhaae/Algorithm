def solution(score):
    s = sorted([sum(i) for i in score])[::-1]
    return [s.index(sum(i))+1 for i in score]