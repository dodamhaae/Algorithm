def solution(id_pw, db):
    if id_pw in db:
            return 'login'
    for i, n in enumerate(db):
        if (id_pw[0] == db[i][0]) & (id_pw[1] != db[i][1]):
            return 'wrong pw'
    return 'fail'