def solution(n, control):
    c = {'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        n+=c[i]
    return n