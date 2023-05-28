def solution(numLog):
    n = ''.join([str(numLog[i]-numLog[i-1]) for i in range(1,len(numLog))])
    return n.replace('-10','a').replace('-1','s').replace('10','d').replace('1','w')