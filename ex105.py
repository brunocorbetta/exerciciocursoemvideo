
def nota(*n, sit = False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >=7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruin'
    return print(r)

nota(5, 6, 7, 8, 9, 10)
