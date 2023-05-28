def solution(myString, pat):
    return 1 if pat in ''.join(['B' if x=='A' else 'A' for x in myString]) else 0