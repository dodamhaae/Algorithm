def solution(x, n):
    sum = 0
    answer=[]
    for i in range(n):
        sum += x
        answer.append(sum)
    return answer