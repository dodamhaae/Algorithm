def solution(k, score):
    return [sorted(score[:i])[::-1][:k][-1] for i in range(1, len(score)+1)] 