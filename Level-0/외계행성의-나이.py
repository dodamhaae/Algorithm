def solution(age):
    answer=''
    age = list(str(age))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in age:
        answer+=alphabet[int(i)]
    return answer