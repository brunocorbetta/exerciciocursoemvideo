print('====================================')
print('====== Corbetta Emprestimos =======')
v_imovel = float(input('Valor do Imovel: '))
s_comprador = float(input('Qual é o seu salario: '))
year = float(input('Em quantos anos quer pagar: '))
year = int(year * 12)
v_parcela = v_imovel / year
margem = s_comprador / 100 * 30

if v_parcela > margem:
    print('Seu emprestimo não foi aprovado')
else:
    print('Seu emprestimo foi aprovado!')
    print('Serão {} parcelas com valor de R${:.2f} cada.'.format(year, v_parcela))







