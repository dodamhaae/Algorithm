def solution(s):
    answer=''
    a = sorted(list(set(s)))
    for i in a:
        if s.count(i) == 1:
            answer+=i
    return answer