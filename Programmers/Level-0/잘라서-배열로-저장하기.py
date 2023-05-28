def solution(my_str, n):
    answer=[]
    s=''
    for i in range(0, len(my_str), n):
        s+=my_str[i:i+n]
        answer.append(s)
        s=''
    return answer