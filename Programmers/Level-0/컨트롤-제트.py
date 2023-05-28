def solution(s):
    answer=0
    s = [x for x in s.split()]
    for i, n in enumerate(s):
        answer+=int(s[i]) if not n=='Z' else -int(s[i-1])
    return answer