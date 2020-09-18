s1 = float(input('Digite o primeiro Segmento: '))
s2 = float(input('Digite o Segundo Seguimento: '))
s3 = float(input('Digite o Terceiro Seguimento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 or s1 == s3 or s2 == s3:
        print('Triangulo Iósceles.')
    elif s1 == s2 and s2 == s3:
        print('Triangulo Equilatéro')
    elif s1 != s2 and s2 != s3:
        print('Triangulo Escaleno.')
else:
    print('Os seguimentos não formar um triangulo!')

