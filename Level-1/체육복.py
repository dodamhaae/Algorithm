def solution(n, lost, reserve):
    answer=[1 for _ in range(n)]
    for i in range(1, n+1):
        if i in lost:
            answer[i-1]-=1
        if i in reserve:
            answer[i-1]+=1
    for i in range(1,len(answer)):
        if 1<i<len(answer):
            if answer[i-1]==0:
                if answer[i-2]==2:
                    answer[i-1]+=1
                    answer[i-2]-=1
                elif answer[i]==2:
                    answer[i]-=1
                    answer[i-1]+=1
        elif i==1:
            if answer[i-1]==0:
                if answer[i]==2:
                    answer[i]-=1
                    answer[i-1]+=1
        if i==len(answer)-1:
            if answer[i]==0:
                if answer[i-1]==2:
                    answer[i-1]-=1
                    answer[i]+=1
    return answer.count(1)+answer.count(2)