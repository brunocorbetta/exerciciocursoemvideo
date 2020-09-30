def area(l, a):
    ar = l * a
    print(f'A area do terreno e {ar:0.2f}m² ')

largura = float(input('Qual é a largura do terreno: '))
compri = float(input('Qual é o comprimento do terreno: '))
area(largura, compri)