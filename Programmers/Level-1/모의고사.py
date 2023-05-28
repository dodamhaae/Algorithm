def solution(answers):
    math1 = [1,2,3,4,5]
    math2 = [2,1,2,3,2,4,2,5]
    math3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt=[0,0,0]
    for i, n in enumerate(answers):
        if answers[i] == math1[i%5]:
            cnt[0]+=1
        if answers[i] == math2[i%8]:
            cnt[1]+=1
        if answers[i] == math3[i%10]:
            cnt[2]+=1
    
    answer = [1, 2, 3]
    for i in range(3):
        if not cnt[i] == max(cnt):
            answer.remove(i+1)
    return answer