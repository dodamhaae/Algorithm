def solution(num_list):
    n1, n2 = 0, 0
    for i in num_list:
        if i%2==0:
            n1 += 1
        else:
            n2 += 1
    return [n1, n2]