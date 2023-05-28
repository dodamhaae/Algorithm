def solution(price):
    if price >= 500000:
        price -= price*0.2
    elif price >= 300000:
        price -= price*0.1
    elif price >= 100000:
        price -= price*0.05
    return int(price)