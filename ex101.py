def voto(nas):
    from datetime import date
    id = date.today().year - nas
    if id < 16:
        return print(f'Você tem {id} anos...Voto Negado!')
    elif (id >= 16 and id < 18) or id > 60:
        return print(f'Você tem {id} anos ...Voto Opcional !')
    else:
        return print(f'Você tem {id} anos..... Voto Obrigatorio')


nasc = int(input('Em que ano você nasceu? '))
voto(nasc)