def solution(n_str):
    n=0
    for s in n_str:
        if s=='0':
            n+=1
        else: break
    return n_str if n==0 else n_str[n:]