def solution(my_string):
    s=''
    my_string = [x for x in my_string.split()]
    answer=[my_string[0]]
    for i in range(1, len(my_string)-1,2):
        answer.append(my_string[i]+my_string[i+1])
    return sum([int(x) for x in answer])