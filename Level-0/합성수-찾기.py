def solution(n):
    answer=0
    for i in range(1, n+1):
        if len([x for x in range(1, i+1) if i%x==0])>=3:
            answer+=1
    return answer