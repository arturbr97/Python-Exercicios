# Faça um Programa que verifique se uma letra digitada é "F" ou "M", representando o sexo de uma pessoa. Conforme
#a letra digitada exibir na tela: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input('Digite (F)-Feminino, (M)-Masculino: ').upper())
if sexo == 'M':
    print('Sexo Masculino.')
elif sexo == 'F':
    print('Sexo Feminino.')
else:
    print('Sexo Inválido.')
