def solution(chicken):
    service=0
    while True:
        if chicken<10: break
        service += chicken//10
        chicken = chicken//10 + chicken%10
    return service