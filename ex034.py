salary = float(input('Digite o salario:'))
if salary > 1250:
    print('O novo salario é R${}'.format(salary + salary / 100 * 10))
else:
    print('O novo salario é R${}'.format(salary + salary / 100 * 15))