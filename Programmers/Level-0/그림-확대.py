def solution(picture, k):
    answer=[]
    for p in picture:
        for _ in range(k):
            answer.append(p.replace('.','.'*k).replace('x','x'*k))
    return answer