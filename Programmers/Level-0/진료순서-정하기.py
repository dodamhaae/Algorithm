def solution(emergency):
    cnt=1
    answer = [0 for _ in range(len(emergency))]
    order= sorted(emergency)[::-1]
    for i in order:
        for j, n in enumerate(emergency):
            if n == i:
                answer[j] = cnt
        cnt+=1
    return answer