def solution(left, right):
    answer=0
    for i in range(left, right+1):
        answer+=i if len([x for x in range(1, i+1) if i%x==0])%2 == 0 else i*-1
    return answer