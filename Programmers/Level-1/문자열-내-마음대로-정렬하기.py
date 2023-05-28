def solution(strings, n):
    answer=[]
    for i in strings:
        answer.append(i[n]+i)
    answer.sort()
    return [x[1:] for x in answer]