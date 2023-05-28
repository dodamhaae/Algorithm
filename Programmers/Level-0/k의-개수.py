def solution(i, j, k):
    answer=''
    for n in range(i, j+1):
        answer+=str(n)
    return answer.count(str(k))