def solution(s):
    cnt,x=0,''
    for i in list(s):
        if i==' ':
            x+=' '
            cnt=0
            continue
        x+=i.upper() if cnt%2==0 else i.lower()
        cnt+=1
    return x