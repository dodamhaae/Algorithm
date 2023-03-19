def solution(n):
    cnt=1
    factorial=1
    while True:
        if factorial>n:
            cnt-=1
            break
        cnt+=1
        print(cnt)
        factorial*=cnt
    return cnt