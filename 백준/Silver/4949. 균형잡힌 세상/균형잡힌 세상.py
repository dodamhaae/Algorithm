import sys

while True:
    s = sys.stdin.readline()
    if s[0]=='.': break
    s = ''.join([i for i in ''.join(s.split()) if i in ['(',')','[',']']])
    while '()' in s or '[]' in s:
        s = s.replace('()','').replace('[]','')
    print('no' if len(s) else 'yes')