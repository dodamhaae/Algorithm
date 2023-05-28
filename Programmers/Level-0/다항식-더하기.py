def solution(polynomial):
    x, n = 0, 0
    poly = [x for x in polynomial.split()]
    for i in poly:
        if i[-1]=='x':
            x+=1 if i == 'x' else int(i[:-1])
        if i.isnumeric():
            n+=int(i)
    if x==0: return str(n)
    if x==1: answer='x'
    elif x>1: answer=str(x)+'x'
    if n!=0: answer+=' + '+str(n)
    return answer