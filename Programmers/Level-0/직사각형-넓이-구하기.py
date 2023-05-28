def solution(dots):
    dots.sort()
    return (dots[2][0]-dots[0][0])*(dots[3][1]-dots[2][1])