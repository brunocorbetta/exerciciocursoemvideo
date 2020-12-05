from ex115.lib.interface import *
from ex115.lib.arquivo import *
from  time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO, Digite uma opção valida!\033[m ')
    sleep(1.5)