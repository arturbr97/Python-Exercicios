#5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
#pelo aluno e apresentar como resultado o seguinte:
#a) A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#b) A mensagem "Reprovado", se a média for menor do que sete;
#c) A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Digite a Primeira Nota: '))
nota2 = float(input('Digite a Segunda Nota: '))

media = (nota1 + nota2) / 2


if media >= 7 and media < 10:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
if media == 10:
        print('Aprovado com Distincao')
