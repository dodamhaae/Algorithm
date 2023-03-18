def solution(num):
    cnt=0
    while num>1:
        cnt+=1
        num=num/2 if num%2==0 else num*3+1
    return cnt if cnt<500 else -1