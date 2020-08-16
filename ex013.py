salary = float(input('Qual é o seu salario atual? R$'))
new_salary = salary + (salary * 15 /100)
#new_salary = salary / 100 * 115
print('Seu novo salario é R$ {:0.2f}'.format(new_salary))