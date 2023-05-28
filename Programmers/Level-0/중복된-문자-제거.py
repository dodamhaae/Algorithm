def solution(my_string):
    answer = ''
    for i in my_string:
        if not i in answer:
            answer+=i
    return answer