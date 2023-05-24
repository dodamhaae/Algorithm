def solution(myString):
    return ''.join([x if x>'l' else 'l' for x in myString])